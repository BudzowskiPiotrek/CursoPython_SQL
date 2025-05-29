import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="appcarloshaya"
)
cursor1 = conexion1.cursor()
cursor1.execute("select id, empleado_dni, dia from turno")
for fila in cursor1:
    print(fila)
conexion1.close()
