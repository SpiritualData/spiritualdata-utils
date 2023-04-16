from spiritualdata_utils import init_logger 
from loguru import logger 
import random, string

init_logger()

def id_generator(append: str = ''):
    """
    The function to generate a unique id
    Length of each id is 10 characters + append string

    Characters can be: 
        1. Digits 
        2. Lower and Upper case letters
        3. Special Characters: @!$

    Parameters
    ----------
    append : str, optional
        The string to append in front of the id to make it recognizable, by default ''
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