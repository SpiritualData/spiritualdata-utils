import os
import pymongo
import loguru


from spiritualdata_utils import init_logger

init_logger()

# Define a cache to store database connections
db_cache = {}

def connect_db(
    uri: str = os.getenv("MONGOURI", None),
    database_name: str = None,
    refresh: bool = False,
):
    """
    This function connects to the MongoDB database using a connection URI.

    Parameters
    ----------
    uri : str
        The MongoDB connection URI
    database_name : str
        The name of the database to connect to
    refresh : bool
        Whether to force a new database connection, by default False

    Returns
    -------
    db
        The MongoDB database object
    """
    # Check if the database connection is cached
    if not refresh and uri in db_cache:
        return db_cache[uri]

    try:
        # Create a new MongoDB client object with the given URI
        client = pymongo.MongoClient(uri)

        # Select the database
        db = client[database_name]

        # Cache the database connection
        db_cache[uri] = db

        return db
    except Exception as e:
        loguru.exception(e)
