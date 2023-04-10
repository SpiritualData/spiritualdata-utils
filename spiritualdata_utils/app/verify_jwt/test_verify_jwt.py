import os
import pytest
from unittest import mock
from spiritualdata_utils import create_jwt, verify_jwt

SECRET_KEY = os.getenv('SECRET_KEY')

def test_create_and_verify_jwt():
    # Define a payload for the JWT
    payload = {'user_id': 1234567890}

    # Create a JWT using the create_jwt function
    jwt_token = create_jwt(payload)

    # Verify the JWT using the verify_jwt function
    decoded_token = verify_jwt(jwt_token)

    # Assert that the decoded token contains the expected user ID
    assert decoded_token['user_id'] == 1234567890
