import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('./example.db')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar una consulta SQL (por ejemplo, obtener las tablas)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Mostrar las tablas
print(tables)

# Si quieres ver los datos de una tabla específica
cursor.execute("SELECT * FROM writes")
#cursor.execute("SELECT * FROM checkpoints")
rows = cursor.fetchall()

# Mostrar las filas
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
