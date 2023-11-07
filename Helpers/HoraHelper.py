# Definición del Helper para el HoraRepository
def hora_helper(hora) -> dict:
    return {
        "id": str(hora["_id"]),
        "hora": hora["hora"],
        "descripcion": hora["descripcion"],
        "hora_pico": hora["hora_pico"],
    }