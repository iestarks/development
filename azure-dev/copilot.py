import requests
from requests.auth import HTTPBasicAuth

# Infoblox and ServiceNow details
infoblox_url = 'https://infoblox.example.com/wapi/v2.7/'
servicenow_url = 'https://devXXXXX.service-now.com/api/now/table/incident'
infoblox_username = 'infoblox_username'
infoblox_password = 'infoblox_password'
servicenow_username = 'servicenow_username'
servicenow_password = 'servicenow_password'

# Authenticate with Infoblox
infoblox_auth = HTTPBasicAuth(infoblox_username, infoblox_password)
infoblox_response = requests.get(infoblox_url, auth=infoblox_auth)

# Authenticate with ServiceNow
servicenow_auth = HTTPBasicAuth(servicenow_username, servicenow_password)
headers = {"Content-Type":"application/json","Accept":"application/json"}
servicenow_response = requests.get(servicenow_url, auth=servicenow_auth, headers=headers)

# Check the responses
if infoblox_response.status_code == 200:
    print("Authenticated with Infoblox successfully.")
else:
    print("Failed to authenticate with Infoblox.")

if servicenow_response.status_code == 200:
    print("Authenticated with ServiceNow successfully.")
else:
    print("Failed to authenticate with ServiceNow.")