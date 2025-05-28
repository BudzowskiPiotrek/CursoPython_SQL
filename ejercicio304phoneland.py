import sqlite3

conexion = sqlite3.connect("CursoPython_SQL/phoneland.db")
conexion.execute(
    "insert into clientes(nombre,apellido,direccion,telefono,cd,ciudad,provincia) values (?,?,?,?,?,?,?)",
    ("Alberto", "Ruiz", "Calle sol", 1111, 29002, "Malaga", "Malaga"),
)
conexion.execute(
    "insert into clientes(nombre,apellido,direccion,telefono,cd,ciudad,provincia) values (?,?,?,?,?,?,?)",
    ("Cristina", "Gomez", "Calle luna", 22222, 29002, "Sevilla", "Sevilla"),
)
conexion.commit()
conexion.close()
