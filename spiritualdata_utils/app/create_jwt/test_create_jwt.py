import os
import pytest
from unittest import mock
from spiritualdata_utils import create_jwt

SECRET_KEY = os.getenv("SECRET_KEY")


def test_create_jwt():
    # Define the input payload
    payload = {"user_id": 1234}

    # Call the create_jwt function
    jwt_token = create_jwt(payload)

    # Assert that a JWT token is returned
    assert type(jwt_token) == str
