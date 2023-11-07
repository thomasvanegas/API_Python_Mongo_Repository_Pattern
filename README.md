# Gestión_Buses_Cargadores_API_Mongo

## Acerca de Este Proyecto

---

El presente proyecto está desarrollado usando:

- Python con el Framework FastAPI
- Capa de Persistencia: MongoDB como motor de BD


## Modelo de Datos

---

El modelo de datos para el presente proyecto se encuentra en el directorio data/script_creacion_modelo_datos_mongodb.txt,
asimismo, los archivos de carga se encuentran en el mismo directorio /data/ con su extensión de archivo .json

## Rutas Disponibles

0. Nota: localhost == 127.0.0.1
1. http://localhost:8000/docs -> Implementación de swagger y visualizar rutas disponibles y sus métodos HTTP asociados
2. http://localhost:8000/api -> Ruta raíz de la api
3. http://localhost:8000/api/buses -> Obtener todos los buses -> Métodos HTTP disponibles: [GET]
4. http://localhost:8000/api/cargadores -> Obtener todos los cargadores -> Métodos HTTP disponibles: [GET]