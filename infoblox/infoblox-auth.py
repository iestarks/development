import requests
from requests.auth import HTTPBasicAuth



# Replace these variables with your actual details
infoblox_url = "https://your-infoblox-instance/wapi/v2.11/"
username = "admin"

# Prompt the user for a password without echoing
password = getpass.getpass("Enter your password: ")

print("Password entered securely.")


