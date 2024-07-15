import requests
import yaml
from requests.auth import HTTPBasicAuth
import getpass

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def call_servicenow_api(config):
    
# Prompt the user for a password without echoing
    password = getpass.getpass("Enter your password: ")
    print("Password entered securely.")
    
    try:
        response = requests.get(
            config['servicenow']['instance_url'] + config['servicenow']['api_endpoint'],
            auth=HTTPBasicAuth(config['servicenow']['username'],password),
            headers={"Accept": "application/json"}
        )
        response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Unexpected error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    config = load_config('config.yaml')
    result = call_servicenow_api(config)
    if result:
        print(result)

if __name__ == "__main__":
    main()