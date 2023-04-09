import os
import pymongo
import pytest
from unittest.mock import MagicMock

from mongo_connect_db import mongo_connect_db

@pytest.fixture
def mock_mongo_client(monkeypatch):
    # Define a mock MongoClient class
    class MockMongoClient:
        def __init__(self, uri):
            pass
        
        def __getitem__(self, database_name):
            return MagicMock()

    # Patch the pymongo.MongoClient class to use the mock class
    monkeypatch.setattr(pymongo, "MongoClient", MockMongoClient)

    # Return the mock MongoClient class
    return MockMongoClient

def test_connect_db(mock_mongo_client):
    # Define test parameters
    uri = "mongodb://localhost/mydb"
    database_name = "mydb"
    refresh = False

    # Call the connect_db() function
    db = connect_db(uri=uri, database_name=database_name, refresh=refresh)

    # Check that the database connection is cached
    assert uri in connect_db.db_cache.keys()

    # Check that the database object is returned
    assert isinstance(db, MagicMock)
