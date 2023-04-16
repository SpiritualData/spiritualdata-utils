from spiritualdata_utils import init_logger 
from loguru import logger 
import random, string

init_logger()

def id_generator(append: str = ''):
    """
    Function to generate a unique ID.

    Args:
        append (str, optional): The string to append in front of the ID to make it recognizable. Default is ''.

    Returns:
        str: A unique ID with a length of 10 characters + the length of the append string.

    Character set:
        * Digits (0-9)
        * Lowercase and uppercase letters (a-z, A-Z)
        * Special characters (@, !, $)
    """
    try:
        id_length = 10
        characters = string.ascii_letters + string.digits + '@!$'
        generated_id = ''.join(random.choice(characters) for i in range(id_length))
        final_id = append + generated_id
        return final_id
    except Exception as e:
        logging.exception(f"Error occurred while generating the ID: {e}")
        return None