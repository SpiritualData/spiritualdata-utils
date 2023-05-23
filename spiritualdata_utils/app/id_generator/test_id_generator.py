import pytest
from spiritualdata_utils import id_generator
import string

def test_id_generator():
    id_length = 10
    append = "Test"
    result = id_generator(append)

    # check if length of id is correct
    assert len(result) == id_length + len(append)

    # check if all characters in the id are valid
    valid_characters = string.ascii_letters + string.digits + "#@!$%&?"
    for char in result:
        assert char in valid_characters

    # check if appended string is present in the id
    assert append in result



