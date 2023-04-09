import os
import pymongo
import pytest
from unittest.mock import MagicMock

from spiritualdata_utils import mongo_connect_db


def test_mongo_connect_db():
    # Define test parameters
    uri = os.getenv("MONGO_URI")
    database_name = os.getenv("MONGO_DB")
    refresh = False

    # Call the connect_db() function
    db = mongo_connect_db(uri=uri, database_name=database_name, refresh=refresh)


    assert db is not None
