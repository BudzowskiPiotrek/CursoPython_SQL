import sqlite3

conexion = sqlite3.connect("CursoPython_SQL/phoneland.db")
try:
    conexion.execute(
        """create table clientes (
                              id integer primary key autoincrement,
                              nombre text,
                              apellido text,
                              direccion text,
                              telefono integer,
                              cd integer,
                              ciudad text,
                              provincia text
                        )"""
    )
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()
