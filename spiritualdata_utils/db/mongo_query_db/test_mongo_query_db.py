import pytest
from pymongo import MongoClient
from spiritualdata_utils import init_logger
from spiritualdata_utils import mongo_connect_db, mongo_query_db
import os


@pytest.fixture(scope="module")
def db():
    # initialize the logger
    init_logger()

    # connect to the test database
    mongo_uri = os.getenv("MONGO_URI")
    database_name = os.getenv("MONGO_DB")
    db = mongo_connect_db(uri=mongo_uri, database_name=database_name, refresh=True)

    # define the test collection
    collection_name = "test_collection"
    collection = db[collection_name]

    # insert some test data
    data_to_insert = {"name": "John Doe", "age": 30}
    inserted_id = mongo_query_db(
        mongo_object=db,
        query_type="insert_one",
        to_insert=data_to_insert,
        collection=collection_name,
    )

    yield db, collection, inserted_id, data_to_insert, collection_name

    # drop the test collection
    collection.drop()


def test_find_data(db):
    # retrieve the necessary variables from the fixture
    db, collection, inserted_id, data_to_insert, collection_name = db

    # check that the inserted ID is not None
    assert inserted_id is not None

    # check that the test data has been inserted
    found_data = mongo_query_db(
        mongo_object=db,
        query_type="find_one",
        query={"name": "John Doe"},
        collection=collection_name,
    )
    assert found_data == data_to_insert


def test_update_data(db):
    # retrieve the necessary variables from the fixture
    db, collection, inserted_id, data_to_insert, collection_name = db

    # update the inserted data
    updated_data = {"name": "Jane Doe", "age": 35}
    result = mongo_query_db(
        mongo_object=db,
        query_type="update_one",
        query={"name": "John Doe"},
        to_insert={"$set": updated_data},
        collection=collection_name,
    )

    # check that the update was successful
    assert result.modified_count == 1

    # check that the updated data is correct
    found_data = mongo_query_db(
        mongo_object=db,
        query_type="find_one",
        query={"name": "Jane Doe"},
        projection={"_id": 0},
        collection=collection_name,
    )
    assert found_data == updated_data
