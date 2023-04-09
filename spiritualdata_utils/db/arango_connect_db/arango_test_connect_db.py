import os
import pytest
from unittest.mock import patch
from arango import ArangoClient
from connect_db import connect_db

@pytest.fixture
def mock_client():
    with patch('arango.ArangoClient') as mock:
        yield mock

def test_connect_db_success(mock_client):
    # mock the ArangoClient and db objects
    mock_db = mock_client.return_value.db.return_value

    # call the function with valid parameters
    db = connect_db(host='myhost', port=1234, database_name='mydatabase',
                    username='myusername', password='mypassword')

    # assert that the ArangoClient was called with the correct parameters
    mock_client.assert_called_once_with(host='myhost', port=1234)

    # assert that the login method was called with the correct parameters
    mock_client.return_value.login.assert_called_once_with(username='myusername', password='mypassword')

    # assert that the db object was returned
    assert db == mock_db

def test_connect_db_failure(mock_client):
    # mock the ArangoClient and db objects to raise an exception
    mock_client.side_effect = Exception("Connection error")

    # call the function with invalid parameters
    db = connect_db(host='invalidhost', port=1234, database_name='mydatabase',
                    username='myusername', password='mypassword')

    # assert that the ArangoClient was called with the correct parameters
    mock_client.assert_called_once_with(host='invalidhost', port=1234)

    # assert that the login method was not called
    mock_client.return_value.login.assert_not_called()

    # assert that None was returned
    assert db is None
