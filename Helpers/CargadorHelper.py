def cargador_helper(cargador) -> dict:
    return {
        "id": str(cargador["_id"]),
        "estado": cargador["estado"],
        "bus_id": str(cargador["bus_id"])
    }