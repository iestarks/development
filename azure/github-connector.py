import requests
from msal import ConfidentialClientApplication
import requests
from azure.identity import DeviceCodeCredential
import os

# Azure AD app credentials
client_id = 'e2074dca-acd2-4e50-96c0-707a0ee78641'
client_secret = os.getenv('AZURE_AD_CLIENT_SECRET')  # It's recommended to use environment variables for secrets
tenant_id = 'c58723e0-75d6-40ab-8459-3c21f3595622'
authority = f'https://login.microsoftonline.com/{tenant_id}'
scope = ['https://graph.microsoft.com/.default']



# Teams and channel information
team_id = '19%3AKh3U4TVii-lqwQ4OftJlWyXb5KeLleBdx0WQb7pAdWc1%40'
channel_id = '19%3A0e48e38376334ae7a0de1d1cc482d814%40'

print("Client Secret" + " " + client_secret)
print("Azure AD app credentials")
print("Client ID" + " " + client_id)
print("Tenant ID" + " " + tenant_id)
print(authority)
print(scope)


# Initialize MSAL
app = ConfidentialClientApplication(client_id, client_secret, authority=authority)
print(app)

# Acquire token using DeviceCodeCredential
credential = DeviceCodeCredential(client_id=client_id, tenant_id=tenant_id)
token_response = app.acquire_token_silent(scopes=scope, account=None, credential=credential)

# Acquire a token
result = app.acquire_token_for_client(scopes=scope)
if "access_token" in result:
    print("Access token acquired:")
    print(result['access_token'])
else:
    print("Failed to acquire token:")
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You might need this when troubleshooting with Microsoft support

if not token_response:
    token_response = app.acquire_token_for_client(scopes=scope)

access_token = token_response['access_token']

# Check if the token_response contains an access_token
if 'access_token' in token_response:
    access_token = token_response['access_token']
else:
    # If 'access_token' is not found, print the error details from the response
    if 'error' in token_response:
        print("Error acquiring token:", token_response['error'])
        print("Error description:", token_response.get('error_description', 'No description available.'))
    else:
        print("Unexpected response structure:", token_response)
    access_token = None  # Ensure access_token is None to avoid further errors

# Proceed only if access_token is not None
if access_token:
    # Prepare the message
    message = {
        "body": {
            "content": "New GitHub Notification: [Link to GitHub Event]",
            "contentType": "html"
        }
    }
    

# Prepare the messageI
message = {
    "body": {
        "content": "New GitHub Notification: [Link to GitHub Event]",
        "contentType": "html"
    }
}

# Send message to Teams channel
graph_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.post(graph_url, json=message, headers=headers)

if response.status_code == 201:
    print("Message sent to Teams successfully.")
else:
    print("Failed to send message to Teams.")
    print("Response:", response.json())
    