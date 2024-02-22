from pymongo import MongoClient
import redis
import pyodbc


#MONGODB

# Conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')

# Selecciona la base de datos MongoDB
mongo_db = mongo_client['nombre_de_tu_base_de_datos']

# Selecciona la colección
mongo_collection = mongo_db['nombre_de_tu_coleccion']



#REDIS

# Conexión al servidor Redis
redis_client = redis.Redis(host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com', port=17069, password= 'grupo5', db=0)



#SQL-SERVER

# Conexión a SQL Server
sql_conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=MONICA;'
                          'DATABASE=ecommerce-web;'
                          'Trusted_Connection=yes;')

# Crea un cursor
cursor = sql_conn.cursor()

# Ingresa el codigo del producto y el codigo del cliente
codigo_producto = input("Ingresa el codigo del producto: ")
codigo_cliente = input("Ingresa el codigo del cliente: ")

# Busca la información del producto en MongoDB
producto_info = mongo_collection.find_one({"codigo": codigo_producto})

# Busca la información del cliente en SQL Server
cursor.execute("SELECT * FROM Usuarios WHERE codigo = ?", codigo_cliente)
cliente_info = cursor.fetchone()

# Verifica si el producto y el cliente existen
if producto_info and cliente_info:
    # Ingresa la cantidad
    cantidad = input("Ingresa la cantidad: ")

    # Crea una clave única para cada cliente
    clave = f'{codigo_cliente}:carrito'

    # Carga los datos en Redis
    redis_client.hset(clave, 'producto', str(producto_info))
    redis_client.hset(clave, 'cantidad', cantidad)
else:
    print("El producto o el cliente no existen.")
