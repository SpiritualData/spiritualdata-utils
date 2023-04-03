import pytest
from api_response import api_response

def test_api_response_with_data():
    expected_response = {"success": True, "data": {"foo": "bar"}}
    assert api_response(data={"foo": "bar"}) == expected_response

def test_api_response_with_message():
    expected_response = {"success": False, "message": "Something went wrong."}
    assert api_response(message="Something went wrong.") == expected_response

