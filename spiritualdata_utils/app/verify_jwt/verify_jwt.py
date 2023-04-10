import os, jwt
from spiritualdata_utils import init_logger
from loguru import logger

init_logger()
SECRET_KEY = os.getenv('SECRET_KEY')


def verify_jwt(jwt_token):
    """
    The function to verify JWT tokens

    Parameters
    ----------
    jwt_token : str
        Check if the jwt token is valid or not

    Returns
    -------
    jwt_token : str
        Decoded jwt token
    """
    try:
        payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        payload["token"] = jwt_token
        if user_id:
            return payload
        raise AuthenticationException(message="Invalid user token")
    except jwt.ExpiredSignatureError as exc:
        logger.exception("Exception :: ", exc_info=True)
        raise TokenExpiredException(
            message="Token has expired, please refresh the token"
        ) from exc
    except Exception as e:
        logger.exception("Exception :: ", exc_info=True)
        raise AuthenticationException(message="Invalid user token") from exc


# Classes for JWT custom exception errors

class AuthenticationException(Exception):
    """Raised when authentication fails due to invalid token."""
    pass

class TokenExpiredException(AuthenticationException):
    """Raised when token has expired."""
    pass
