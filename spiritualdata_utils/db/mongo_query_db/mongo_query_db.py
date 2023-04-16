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
    The function to run various mongo queries for the spiritual_data codebase

    Parameters
    ----------
    mongo_object : MongoClient
        Mongo object that the queries need to run on, a db connection
    query_type : str
        Choices from find, find_one, insert, insert_one, update, update_one
    query : dict, optional
        The query to be run, by default None
    to_insert : dict, optional
        If something is to be inserted or updated, by default None
    collection : str
        the collection to query on, by default None
    projection : dict, optional
        The projection to apply to the query, by default None

    Returns
    -------
    result : dict or None
        The result of the query
    """
    logger.debug(
        f"Running mongo_query_db with query_type: {query_type}, query: {query}, to_insert: {to_insert}, collection: {collection}, and projection: {projection}"
    )
    if collection is None:
        raise ValueError("Collection name is required")

    if query_type == "find":
        result = mongo_object[collection].find(query, projection)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and projection: {projection}"
        )
        return [r for r in result]

    elif query_type == "find_one":
        result = mongo_object[collection].find_one(query, projection)
        logger.debug(
            f"Mongo query {query_type} on collection {collection} with query: {query} and projection: {projection}"
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
