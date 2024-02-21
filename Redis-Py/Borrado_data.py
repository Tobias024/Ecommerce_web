# Redis
import redis

# Crear una conexión a Redis
r = redis.Redis(
    host='redis-17069.c267.us-east-1-4.ec2.cloud.redislabs.com',  # El host de tu servidor Redis
    port=17069,  # El puerto de tu servidor Redis
    password= 'grupo5',
    db=0  # El número de base de datos a la que quieres conectarte
)

# Vaciar la base de datos
r.flushdb()
