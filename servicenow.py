import requests
from requests.auth import HTTPBasicAuth

# Replace these variables with your actual details
instance = "your_instance_name"
user = "ncsu.ee2017@gmail.com"
pwd = "Hond@135"
incident_sys_id = "incident_sys_id_here"  # Use sys_id or a query to identify the specific incident

# ServiceNow API endpoint for the incident table
url = f"https://{instance}.service-now.com/api/now/table/incident/{incident_sys_id}"

# Set proper headers
headers = {"Accept": "application/json"}

# Do the HTTP request
response = requests.get(url, auth=HTTPBasicAuth(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)