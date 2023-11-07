# Definición del Helper para el BusRepository
def bus_helper(bus) -> dict:
    return {
        "id": str(bus["_id"]),
        "placa": bus["placa"],
        "marca": bus["marca"],
        "estado": bus["estado"],
        "ult_hora_carga": bus["ult_hora_carga"]
    }