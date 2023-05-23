from spiritualdata_utils import init_logger
from loguru import logger
from pymongo import MongoClient, ReturnDocument

init_logger()


def mongo_query_db(
    mongo_object: MongoClient,
    query_type: str,
    query: dict = None,
    to_insert: dict = None,
    collection: str = None,
    projection: dict = None,
):
    """
    Runs various MongoDB queries for the spiritual_data codebase.

    Args:
        mongo_object (MongoClient): The MongoDB client object.
        query_type (str): The type of query to run. Choices are: find, find_one, insert, insert_one, update, update_one.
        collection (str): The collection to query on.
        query (dict, optional): The query to be run. Default is None.
        to_insert (dict, optional): If something is to be inserted or updated. Default is None.
        projection (dict, optional): The projection to apply to the query. Default is None.

    Returns:
        dict or None: The result of the query.
    """
    logger.debug(
        f"Running mongo_query_db with query_type: {query_type}, query: {query}, to_insert: {to_insert}, collection: {collection}, and projection: {projection}"
    )
    if collection is None:
        raise ValueError("Collection name is required")

    if query_type == "find":
        if projection == None:
            projection = {"_id": 0}
        else:
            projection = {"_id": 0, **projection}
        result = mongo_object[collection].find(query, projection)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and projection: {projection}"
        )
        return [r for r in result]

    elif query_type == "find_one":
        if projection == None:
            projection = {"_id": 0}
        else:
            projection = {"_id": 0, **projection}
        result = mongo_object[collection].find_one(query, projection)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and projection: {projection}, result: {result}"
        )
        return result

    elif query_type == "insert":
        result = mongo_object[collection].insert(to_insert)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with to_insert: {to_insert}"
        )
        return result

    elif query_type == "insert_one":
        result = mongo_object[collection].insert_one(to_insert)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with to_insert: {to_insert}"
        )
        return result

    elif query_type == "update":
        result = mongo_object[collection].update(query, to_insert)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and to_insert: {to_insert}"
        )
        return result

    elif query_type == "update_one":
        result = mongo_object[collection].update_one(query, to_insert, upsert=True)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and to_insert: {to_insert}"
        )
        return result

    else:
        raise ValueError("Invalid query type")
