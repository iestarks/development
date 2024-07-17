from unittest.mock import patch
import pytest
from your_app_module import initialize_msal

@patch('msal.ConfidentialClientApplication')
def test_token_acquisition(mock_msal):
    # Setup mock response
    mock_msal.return_value.acquire_token_for_client.return_value = {'access_token': 'test_token'}

    # Call the function that initializes MSAL and acquires a token
    token_response = initialize_msal()

    # Assert that the token was acquired successfully
    assert token_response['access_token'] == 'test_token'