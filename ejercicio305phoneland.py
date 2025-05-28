import sqlite3

conexion = sqlite3.connect("CursoPython_SQL/phoneland.db")

cursor = conexion.execute(
    "select id,nombre,apellido,direccion,telefono,cd,ciudad,provincia from clientes"
)

for fila in cursor:
    print(fila)
conexion.close()
