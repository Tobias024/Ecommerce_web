from pymongo import MongoClient
import redis
import pyodbc
from datetime import datetime
import uuid

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
    # Autenticación de usuario con correo electrónico
    correo_usuario = input("Ingresa tu correo electrónico: ")
    cursor.execute("SELECT * FROM Usuarios WHERE mail = ?", correo_usuario)
    cliente_info = cursor.fetchone()
    if cliente_info:
        print("Usuario encontrado. Por favor, ingresa tu clave.")
        clave_ingresada = input("Clave: ")
        if cliente_info.clave == clave_ingresada:
            print("Usuario autenticado correctamente.")
            codigo_cliente = cliente_info.uuid
        else:
            print("Clave incorrecta. Intente nuevamente.")
            exit()
    else:
        print("El correo electrónico no está registrado. Creando nuevo usuario...")
        # Generar un UUID aleatorio no repetido
        codigo_cliente = str(uuid.uuid4())

        # Permitir ingresar los datos del nuevo usuario
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        clave = input("Clave: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        rol_id = 3

        # Guardar el nuevo usuario en la tabla Usuarios
        cursor.execute("INSERT INTO Usuarios (uuid, nombre, apellido, clave, direccion, telefono, mail, rol_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       codigo_cliente, nombre, apellido, clave, direccion, telefono, correo_usuario, rol_id)
        sql_conn.commit()
        print("Nuevo usuario creado correctamente.")

    # Recuperación o creación de sesión de usuario en SQL
    cursor.execute("SELECT * FROM Usuarios WHERE uuid = ?", codigo_cliente)
    sesion_info = cursor.fetchone()
    if sesion_info:
        print("Sesión de usuario recuperada.")
    else:
        fecha_sesion = datetime.now()
        cursor.execute("INSERT INTO Usuarios (uuid, fecha_sesion) VALUES (?, ?)", codigo_cliente, fecha_sesion)
        sql_conn.commit()
        print("Sesión de usuario creada.")

    # Categorización de usuario
    cursor.execute("SELECT COUNT(*) FROM Pagos WHERE uuid = ?", codigo_cliente)
    cantidad_compras = cursor.fetchone()[0]
    if cantidad_compras >= 10:
        categoria = "TOP"
    elif cantidad_compras >= 5:
        categoria = "MEDIUM"
    else:
        categoria = "LOW"
    print(f"Categoría del usuario: {categoria}")

    # Ingresa el código del producto
    codigo_producto = input("Ingresa el código del producto: ")

    # Busca la información del producto en MongoDB
    producto_info = mongo_collection.find_one({"_id": codigo_producto})

    # Verifica si el producto existe
    if producto_info:
        try:
            # Ingresa la cantidad
            cantidad = int(input("Ingresa la cantidad: "))

            # Crea una clave única para cada cliente
            clave = f'{codigo_cliente}:carrito'

            # Calcula el monto
            monto = cantidad * producto_info['precio']

            # Carga los datos en Redis
            redis_client.hset(clave, 'producto', str(producto_info))
            redis_client.hset(clave, 'cantidad', cantidad)
            print("Producto agregado al carrito con éxito.")

            # Registra el pago en la tabla Pagos
            pago_id = str(uuid.uuid4())
            fecha_pago = datetime.now()
            cursor.execute("INSERT INTO Pagos (pago_id, monto, fecha, usuario_id) VALUES (?, ?, ?, ?)", pago_id, monto, fecha_pago, codigo_cliente)
            sql_conn.commit()
            print("Pago registrado correctamente.")
        except ValueError:
            print("La cantidad debe ser un número entero.")
    else:
        print("El producto no existe.")

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")

finally:
    # Cierra las conexiones
    cursor.close()
    sql_conn.close()
