from arango import ArangoClient
import os
from loguru import logger
from spiritualdata_utils import init_logger

init_logger()

def arango_connect_db(
    host: str = "localhost",
    port: int = 8529,
    database_name: str = None,
    username: str = os.getenv("USERNAME", None),
    password: str = os.getenv("PASSWORD", None),
):
    """
    This function connects to the ArangoDB database.

    Parameters
    ----------
    host : str, optional
        The host string where Arangodb is hosted, by default "localhost"
    port : int, optional
        The port at which Arangodb is running on, by default 8529
    database_name : str
        The database, by default None
    username : str, optional
        The username of the user who will be using the db, by default os.getenv("USERNAME", None)
    password : str, optional
        The, by default os.getenv("PASSWORD", None)

    Returns
    -------
    db
        The arangodb database object
    """
    try:
        # Create a new ArangoDB client object
        client = ArangoClient(host, port)

        # Authenticate with the given username and password (if provided)
        if username and password:
            client.login(username=username, password=password)

        # Select the database
        db = client.db(database_name)

        return db
    except Exception as e:
        loguru.exception(e)
