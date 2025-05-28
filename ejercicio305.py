import sqlite3

conexion = sqlite3.connect("CursoPython_SQL/bd1.db")
cursor = conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()
