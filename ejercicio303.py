import sqlite3

conexion = sqlite3.connect("sql/bd1.db")
try:
    conexion.execute(
        """create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )"""
    )
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()
