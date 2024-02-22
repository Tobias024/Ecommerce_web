from pymongo import MongoClient
import redis
import pyodbc

# Conexión a MongoDB
mongo_client = MongoClient("mongodb+srv://bd2:grupo5@cluster0.lh9bhcb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client['Ecommerce']
mongo_collection = mongo_db['Productos']

# Conexión al servidor Redis
redis_client = redis.Redis(host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com', port=17069, password='grupo5', db=0)

# Conexión a SQL Server
sql_conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=MONICA;'
                          'DATABASE=ecommerce-web;'
                          'Trusted_Connection=yes;')

# Crea un cursor
cursor = sql_conn.cursor()

try:
    # Ingresa el código del producto y el código del cliente
    codigo_producto = input("Ingresa el código del producto: ")
    codigo_cliente = input("Ingresa el código del cliente: ")

    # Busca la información del producto en MongoDB
    producto_info = mongo_collection.find_one({"_id": codigo_producto})

    # Busca la información del cliente en SQL Server
    cursor.execute("SELECT * FROM Usuarios WHERE uuid = ?", codigo_cliente)
    cliente_info = cursor.fetchone()

    # Verifica si el producto y el cliente existen
    if producto_info and cliente_info:
        try:
            # Ingresa la cantidad
            cantidad = int(input("Ingresa la cantidad: "))

            # Crea una clave única para cada cliente
            clave = f'{codigo_cliente}:carrito'

            # Carga los datos en Redis
            redis_client.hset(clave, 'producto', str(producto_info))
            redis_client.hset(clave, 'cantidad', cantidad)
            print("Producto agregado al carrito con éxito.")
        except ValueError:
            print("La cantidad debe ser un número entero.")
    else:
        print("El producto o el cliente no existen.")

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")

finally:
    # Cierra las conexiones
    cursor.close()
    sql_conn.close()
