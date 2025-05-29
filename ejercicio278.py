import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="appgym"
)
cursor1 = conexion1.cursor()
sql = "insert into usuario(nombre_usuario, contraseña, correo) values (%s,%s,%s)"
datos = ("Carla_222", "1234QWER", "dasnjdas@hotmail.com")
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
