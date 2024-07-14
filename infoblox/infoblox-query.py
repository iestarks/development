import infoblox
import servicenow.servicenow as sn 

def get_infoblox_url():
    # Get the Infoblox URL from the configuration file
    config = inflobox.get_config()
    return config["infoblox"]["url"]

def get_incident_data(instance, user, password, incident_sys_id):
    # ServiceNow API endpoint for the incident table
    url = f"https://{instance}.service-now.com/api/now/table/incident/{incident_sys_id}"
    
    # Set proper headers
    headers = {"Accept": "application/json"}
    
    # Do the HTTP request
    response = requests.get(url, auth=HTTPBasicAuth(user, password), headers=headers)
    
    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        return None
    
    # Decode the JSON response into a dictionary and return the data
    return response.json()

# Example: Query for an A record
def query_a_record(record_name):
    # Get the Infoblox URL
    infoblox_url = get_infoblox_url()
    
    # Set the query parameters
    query_type = "record:a"
    
    # Formulate the query URL
    query_url = f"{infoblox_url}{query_type}?name={record_name}"
    
    # Perform the query
    response = requests.get(query_url, auth=HTTPBasicAuth(username, password))
    
    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        return None
    
    # Decode the JSON response into a dictionary and return the data
    return response.json()