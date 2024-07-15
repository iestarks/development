import requests
from requests.auth import HTTPBasicAuth
import json
import getpass

class servicenow_auth:
    def __init__(self, instance, user, password):
        self.instance = instance
        self.user = user
        self.password = password
    
    def __str__(self):
        return f"ServiceNow instance: {self.instance}, User: {self.user}"
    
    def service_auth(self):
        # Attempt to authenticate to the ServiceNow instance
        response = requests.get(self.instance, auth=HTTPBasicAuth(self.user, self.password))
        
        # Check if the authentication was successful
        if response.status_code == 200:
            print("Authentication successful!")
        else:
            print(f"Authentication failed! Status code: {response.status_code}")
        
        return response


class add_sys_user(servicenow_auth):

    def add_sys_user(self, user_data):
        # ServiceNow API endpoint for the incident table
        url = f"https://{self.instance}.service-now.com/api/now/table/sys_user"
        
        # Set proper headers
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        
        # Do the HTTP request
        response = requests.post(url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, json=user_data)
        
        # Check for HTTP codes other than 201
        if response.status_code != 201: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
            return None
        
        # Decode the JSON response into a dictionary and return the data
        return response.json()
        
class create_change_request(servicenow_auth):
    
    def create_change_ticket(self, change_data):
        # ServiceNow API endpoint for the incident table
        url = f"https://{self.instance}.service-now.com/api/now/table/change_request"
        reason = "Scheduled Maintenance"
        change_data["reason"] = reason
        
        
        # Set proper headers
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        
        # Do the HTTP request
        response = requests.post(url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, json=change_data)
        
        # Check for HTTP codes other than 201
        if response.status_code != 201: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
            return None
        
        # Decode the JSON response into a dictionary and return the data
        return response.json()
    
       
class get_incident_data(servicenow_auth):
    
    def get_incident_data(self, incident_sys_id):
        # ServiceNow API endpoint for the incident table
        url = f"https://{self.instance}.service-now.com/api/now/table/incident/{incident_sys_id}"
        
        # Set proper headers
        headers = {"Accept": "application/json"}
        
        # Do the HTTP request
        response = requests.get(url, auth=HTTPBasicAuth(self.user, self.password), headers=headers)
        
        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
            return None
        
        # Decode the JSON response into a dictionary and return the data
        return response.json()
        
        
        
        

        
        

