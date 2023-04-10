import os, jwt 
from spiritualdata_utils import init_logger
from loguru import logger

init_logger()
SECRET_KEY = os.environ.get('SECRET_KEY')

def create_jwt(data):
    """
    The function to issue a JWT

    Parameters
    ----------
    data : dict
        Payload to store in JWT

    Returns
    -------
    string
        jwt_token that is returned for the data.
    """
    try:
        logger.info(f"Encoding the payload: {data}")
        token = jwt.encode(data, SECRET_KEY)
        return token
    except Exception as e:
        logger.exception(f"Error while encoding the payload: {e}")
        return None