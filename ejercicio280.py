import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="appgym"
)
cursor1 = conexion1.cursor()
cursor1.execute("delete from usuario where id=4")
cursor1.execute("update usuario set tipo='Administrador' where id=3")
conexion1.commit()
cursor1.execute("select id, nombre_usuario, tipo from usuario")
for fila in cursor1:
    print(fila)
conexion1.close()
