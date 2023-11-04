# Servicio para obtener un solo bus -> find_bus_by_id
def BusService(bus) -> dict:
    return {
        # "id": bus["_id"],
        "placa": bus["placa"],
        "marca": bus["marca"],
        "estado": bus["estado"],
        "ult_hora_carga": bus["ult_hora_carga"]
    }


# Servicio para obtener todos los buses -> find_all_buses
def BusesService(buses_list) -> list:
    return [BusService(bus) for bus in buses_list]