

# Import the function from the servicenow module
from servicenow import get_incident_data
from servicenow_auth import instance, username, password
import json
import requests 
from requests.auth import HTTPBasicAuth


# Prompt the user for the incident sys_id
#ask_user = input("Enter the incident #: ")  # Use sys_id or a query to identify the specific incident
#incident_sys_id = ask_user

incident_sys_id = "00013817c3138610b6b4f6edd401314b"

# # Call the function
# response = get_incident_data(incident_sys_id, username, password)

# print(response)

# print("Incident data retrieved successfully!")

# Print the response

# Make the POST request to Print out the INC# and the sys_id
instance = "https://dev249066.service-now.com/api/now/table/"
url = f"{instance}/incident/{incident_sys_id}"

response = requests.get(url, auth=HTTPBasicAuth(username, password))
print(response.json())
