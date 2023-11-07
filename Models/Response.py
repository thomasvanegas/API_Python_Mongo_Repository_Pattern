def Response(data, mensaje) -> dict:
    return {
        "data": [data],
        "code": 200,
        "message": mensaje,
    }