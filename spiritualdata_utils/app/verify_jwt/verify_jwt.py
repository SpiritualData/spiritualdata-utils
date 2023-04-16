import os, jwt
from fastapi import Depends, HTTPException, Header
from spiritualdata_utils import init_logger
from fastapi.security import HTTPBearer
from loguru import logger

init_logger()
SECRET_KEY = os.getenv("SECRET_KEY")
oauth2_scheme = HTTPBearer()


class verify_jwt(object):
    """
    Class for verifying JWT tokens.

    Notes:
        * This is a class because functions cannot handle parameters with a function for dependency injection.
    """

    def verify_jwt_func(self, jwt_token=Depends(oauth2_scheme)):
        """
        Verify if the JWT token is valid or not.

        Args:
            jwt_token (str): The JWT token to verify.

        Returns:
            str: The decoded JWT token.

        """
        try:
            if type(jwt_token) != str:
                # For swagger doc
                jwt_token = jwt_token.credentials
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            payload["token"] = jwt_token
            if user_id:
                return payload
            raise AuthenticationException(message="Invalid user token")
        except jwt.ExpiredSignatureError as e:
            logger.exception("Exception :: ", exc_info=True)
            raise TokenExpiredException(
                message="Token has expired, please refresh the token"
            ) from e
        except Exception as e:
            logger.exception("Exception :: ", exc_info=True)
            raise AuthenticationException(message="Invalid user token") from e


# Classes for JWT custom exception errors


class AuthenticationException(Exception):
    """Raised when authentication fails due to invalid token."""

    def __init__(self, message="Invalid Input Provided"):
        super(AuthenticationException, self).__init__(message)
        self.status = 403


class TokenExpiredException(Exception):
    """Raised when token has expired."""

    def __init__(self, message="Invalid Input Provided"):
        super(TokenExpiredException, self).__init__(message)
        self.status = 403
