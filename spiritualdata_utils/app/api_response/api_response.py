def api_response(data: any = None, message: str = None):
    """
    Function to create a standard API response for the entire codebase.

    Args:
        data (Any): Data to send back to the frontend.
        message (str): Message to send back to the frontend when an error occurs.

    Returns:
        dict: A dictionary containing the API response.
        
    Benefits:
        * Developers only need to send the data/message, as the `api_response` function handles all response level actions.
    """


    if data:
        return {"success": True, "data": data}
    if message:
        return {"success": False, "message": message}
