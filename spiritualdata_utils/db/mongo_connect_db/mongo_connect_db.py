import os
import pymongo
from loguru import logger


from spiritualdata_utils import init_logger

init_logger()

# Define a cache to store database connections
db_cache = {}


def mongo_connect_db(
    uri: str = os.getenv("MONGOURI", None),
    database_name: str = None,
    refresh: bool = False,
):
    """
    Connects to the MongoDB database using a connection URI.

    Args:
        uri (str): The MongoDB connection URI.
        database_name (str): The name of the database to connect to.
        refresh (bool, optional): Whether to force a new database connection. Default is False.

    Returns:
        Database: The MongoDB database object.
    """
    # Check if the database connection is cached
    key = f"{uri}/{database_name}"
    if not refresh and key in db_cache:
        return db_cache[key]

    try:
        # Create a new MongoDB client object with the given URI
        logger.debug("Connecting to MongoDB...")

        client = pymongo.MongoClient(uri)

        # Select the database
        db = client[database_name]

        # Cache the database connection
        db_cache[key] = db

        return db
    except Exception as e:
        logger.exception(e)
        return None
