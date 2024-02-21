"""# MongoDB
from pymongo import MongoClient

def get_mongodb_data():
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    collection = db.test
    data = collection.find({})
    return data


# MySQL
import mysql.connector

def get_mysql_data():
    cnx = mysql.connector.connect(user='<username>', password='<password>',
                                  host='127.0.0.1',
                                  database='test')
    cursor = cnx.cursor()
    query = ("SELECT * FROM test")
    cursor.execute(query)
    data = cursor.fetchall()
    return data
    """

"""
# Redis
import redis
import json

try:
    # Crear una conexión a Redis
    r = redis.Redis(
        host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com',  # El host de tu servidor Redis
        port=17069,  # El puerto de tu servidor Redis
        password= 'grupo5',
        db=0  # El número de base de datos a la que quieres conectarte
    )

    # Intenta hacer una operación simple (como obtener todas las claves)
    r.keys()

    print("Conexión exitosa al servidor Redis.")
except Exception as e:
    print(f"Error al conectarse al servidor Redis: {e}")

# Obtener todas las claves
claves = r.keys()

# Iterar sobre las claves para obtener sus valores
for clave in claves:
    tipo = r.type(clave)
    if tipo == b'string':
        valor = r.get(clave).decode('utf-8')
        valor_json = json.dumps(valor)
        print(f'{clave.decode("utf-8")}: {valor_json}')
"""

import redis
import json

try:
    # Crear una conexión a Redis
    r = redis.Redis(
        host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com',  # El host de tu servidor Redis
        port=17069,  # El puerto de tu servidor Redis
        password= 'grupo5',
        db=0  # El número de base de datos a la que quieres conectarte
    )

    # Intenta hacer una operación simple (como obtener todas las claves)
    claves = r.keys()
    print(f"Claves obtenidas: {claves}")

    print("Conexión exitosa al servidor Redis.")
except Exception as e:
    print(f"Error al conectarse al servidor Redis: {e}")

# Iterar sobre las claves para obtener sus valores
for clave in claves:
    tipo = r.type(clave)
    if tipo == b'string':
        valor = r.get(clave).decode('utf-8')
        print(f'{clave.decode("utf-8")}: {valor}')
