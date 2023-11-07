# Gestión_Buses_Cargadores_API_Mongo

## Acerca de Este Proyecto

---

El presente proyecto está desarrollado usando:

- Python con el Framework FastAPI
- Capa de Persistencia: MongoDB como motor de BD


## Modelo de Datos

---

El modelo de datos para el presente proyecto se encuentra en el directorio **data/script_creacion_modelo_datos_mongodb.txt**,
asimismo, los archivos de carga se encuentran en el mismo directorio **/data/ con su extensión de archivo .json**

## Rutas Disponibles

0. Nota: localhost == 127.0.0.1
1. http://localhost:8000/docs -> Implementación de swagger y visualizar rutas disponibles y sus métodos HTTP asociados
2. http://localhost:8000/ -> Ruta raíz
3. http://localhost:8000/api/cargadores/ -> Todos los Métodos HTTP disponibles [GET, POST, PUT, DELETE] <-> [CREATE, READ, UPDATE, DELETE]
4. http://localhost:8000/api/buses/ -> Todos los Métodos HTTP disponibles [GET, POST, PUT, DELETE] <-> [CREATE, READ, UPDATE, DELETE]
5. http://localhost:8000/api/horas/ -> Todos los Métodos HTTP disponibles [GET, POST, PUT, DELETE] <-> [CREATE, READ, UPDATE, DELETE]

## Instalación de Dependencias
---

Para **Instalar y Ejecutar Correctamente** se deben cumplir los siguientes requisitos:

1. Instalar Python en su version 3.12.0 -> En esta versión se activan las TASKS AND CORRUTINES lo que permite ASYNC-AWAIT
2. Ejecutar el siguiente comando: pip install -r requirements.txt  --> Este archivo contiene las dependencias necesarias
    las cuales son: FastAPI, Uvicorn, Motor, Pymongo, etc...

## ¿Cómo Ejecutar el Proyecto?

- ejecutar el Comando: 

1. python -m uvicorn main:app --reload

ó en su defecto:

2. también uvicorn main:app --reload (De no funcionar la opción del literal 1)

## Estudiantes del Proyecto

1. Estudiante N°1: Thomas Camilo Vanegas Acevedo - ID: 000287437 - thomas.vanegasa@upb.edu.co
2. Estudiante N°2: Eliana Giraldo Duque - ID: 000321721 - eliana.giraldod@upb.edu.co