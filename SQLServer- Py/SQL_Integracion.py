import pyodbc

# Cadena de conexión a la base de datos -> mysql server
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=MONICA;' #Su Servidor
    r'DATABASE=ecommerce-web;'
    r'Trusted_Connection=yes;'
)

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)

# Crear un cursor
cur = conn.cursor()

# Realizar una consulta SQL
cur.execute("SELECT * FROM Usuarios")

# Obtener los resultados
resultados = cur.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión
conn.close()

