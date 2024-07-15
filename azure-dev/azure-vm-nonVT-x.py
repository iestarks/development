from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption
import json

import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', category=InsecureRequestWarning)

# Azure details
subscription_id = '26017051-b218-4c95-87bd-0f2beb745bf3'
resource_group = 'starksenterprise.com'
vm_name = 'vm-mgmt'  # replace with your VM name
location = 'eastus'

# Get credentials
credential = DefaultAzureCredential()

# Create clients
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)


### Create Virtual Network

vnet_params = {
    'location': location,  # replace with your desired location
    'address_space': {
        'address_prefixes': ['172.16.0.0/16']
    }
}

vnet = network_client.virtual_networks.begin_create_or_update(
    resource_group,  # replace with your resource group name
    'vm-mgmt-nic',  # replace with your desired virtual network name
    vnet_params
).result()

### Create Subnet

subnet_params = {
    'address_prefix': '172.16.0.0/16'
}

subnet = network_client.subnets.begin_create_or_update(
    resource_group,  # replace with your resource group name
    vnet.name,  # replace with your virtual network name
    'vm-mgmt-subnet',  # replace with your desired subnet name
    subnet_params
).result()



# Create Public IP

public_ip_params = {
    'location': location,  # replace with your desired location
    'public_ip_allocation_method': 'Dynamic'
}

public_ip_address = network_client.public_ip_addresses.begin_create_or_update(
    resource_group,  # replace with your resource group name
    'vm-mgmt-pub-ip',  # replace with your desired public IP name
    public_ip_params
).result()

##### Create Virtual Network Interface Card

nic_params = {
    'location': location,  # replace with your desired location
    'ip_configurations': [{
        'name': 'vm-mgmt-ip-config',  # replace with your desired IP configuration name
        'public_ip_address': {
            'id': public_ip_address.id
        },
        'subnet': {
            'id': subnet.id
        }
    }]
}

nic = network_client.network_interfaces.begin_create_or_update(
    resource_group,  # replace with your resource group name
    'vm-mgmt-nic',  # replace with your desired NIC name
    nic_params
).result()


# Create VM
vm_parameters = {
    'location': location,  # replace with your location
    'hardware_profile': {
        'vm_size': 'Standard_D8s_v3'  # replace with your VM size
    },
    'storage_profile': {
        'image_reference': {
            'publisher': 'MicrosoftWindowsServer',
            'offer': 'WindowsServer',
            'sku': '2016-Datacenter',
            'version': 'latest'
        }
    },
    'network_profile': {
        'network_interfaces': [{
            'id': network_client.network_interfaces.get(
                resource_group,
                vnet.name # replace with your network interface card name
            ).id
        }]
    },
    'os_profile': {
        'computer_name': vm_name,
        'admin_username': 'vm-mgmt',  # replace with your username
        'admin_password': 'Vm-password2024'  # replace with your password
    }
}

operation = compute_client.virtual_machines.begin_create_or_update(
    resource_group,
    vm_name,
    vm_parameters
)

operation.wait()


### Create Security Group

nsg_params = {
    'location': location # replace with your desired location
}

nsg = network_client.network_security_groups.begin_create_or_update(
    resource_group,  # replace with your resource group name
    'vm-mgmt',  # NSG name
    nsg_params
).result()

### Create a security rule to open the RDP port:
security_rule_params = {
    'protocol': 'Tcp',
    'source_address_prefix': '*',
    'destination_address_prefix': '*',
    'access': 'Allow',
    'direction': 'Inbound',
    'source_port_range': '*',
    'destination_port_range': '3389',
    'priority': 1000
}

security_rule = network_client.security_rules.begin_create_or_update(
    resource_group,  # replace with your resource group name
    'vm-mgmt',  # NSG name
    'mySecurityRule',  # replace with your desired security rule name
    security_rule_params
).result()