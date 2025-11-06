import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user="tu_usuario",
                                  passwd="tu_contraseña",
                                  database="dvwa")
cursor1=conexion1.cursor()
cursor1.execute("delete from security_log where id=1")
cursor1.execute("update access_log set action=\"adios\" where id=3")
cursor1.execute("select * from access_log")
for fila in cursor1:
    print(fila)
conexion1.commit()
conexion1.close()
