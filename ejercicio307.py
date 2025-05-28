import sqlite3

conexion=sqlite3.connect("CursoPython_SQL/bd1.db")
codigo=int(input("Ingrese el código de un artículo:"))

cursor=conexion.cursor
cursor=conexion.execute("delete from articulos where codigo=?", (codigo, ))

print ("filas borradas",cursor.rowcount)
conexion.commit

conexion.close()