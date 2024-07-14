import requests
from requests.auth import HTTPBasicAuth
import json
import getpass

# Replace these variables with your actual details
instance = "dev249066"
user = "admin"  # Use your own username
incident_sys_id = "a83820b58f723300e7e16c7827bdeed2"  # Use sys_id or a query to identify the specific incident

# Prompt the user for a password without echoing
password = getpass.getpass("Enter your password: ")

print("Password entered securely.")
# ServiceNow API endpoint for the incident table
url = f"https://{instance}.service-now.com/api/now/table/incident/{incident_sys_id}"

# Set proper headers
headers = {"Accept": "application/json"}

# Do the HTTP request
response = requests.get(url, auth=HTTPBasicAuth(user, password), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(json.dumps(data, indent=4))  # Print the JSON response with indentation
