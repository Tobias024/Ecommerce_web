import redis
import random

# Crear una conexión a Redis
r = redis.Redis(
    host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com',  # El host de tu servidor Redis
    port=17069,  # El puerto de tu servidor Redis
    password='grupo5',  # La contraseña de tu servidor Redis
    db=0  # El número de base de datos a la que quieres conectarte
)

# Lista de productos tecnológicos
productos = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Cámara', 'Auriculares', 'Altavoz Bluetooth', 'Monitor', 'Teclado', 'Ratón', 'Impresora', 'Router', 'Disco duro externo', 'Pendrive', 'Tarjeta de memoria', 'Cargador portátil', 'Proyector', 'Micrófono', 'Webcam', 'Drone']

# Crear 20 claves y valores
for i in range(20):
    clave = productos[i]  # Usar el nombre del producto como clave
    valor = {'producto': productos[i], 'cantidad': random.randint(1, 5)}
    for campo, valor_campo in valor.items():
        r.hset(clave, campo, valor_campo)


