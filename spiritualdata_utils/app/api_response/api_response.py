def api_response(data: any = None, message: str = None):
    """
    This function is used to create a standard API response for the entire codebase
    In this format, the benefit is:
        1. Developer only needs to send data/message, api_response will be handling all response level actions

    Parameters
    ----------
    data : any
        What data to send back to the frontend.
    message : str
        What message to send back to the frontend when it fails
    """

    if data:
        return {"success": True, "data": data}
    if message:
        return {"success": False, "message": message}
