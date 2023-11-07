def ErrorResponse(error, code, message) -> dict:
    return {"error": error, "code": code, "message": message}