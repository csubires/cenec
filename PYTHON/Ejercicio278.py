import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user="tu_usuario",
                                  passwd="tu_contraseña",
                                  database="dvwa")
cursor1=conexion1.cursor()
sql="insert into access_log(user_id, target_id, action, timestamp) values (%s, %s,%s, %s)"
datos=(1, 1, 'Ninguna', '2025-10-12')
cursor1.execute(sql, datos)
datos=(2, 2, 'Ninguna', '2025-10-12')
cursor1.execute(sql, datos)
datos=(3, 3, 'Ninguna', '2025-10-12')
cursor1.execute(sql, datos)

def get_float(mensaje):
    try:
        return float(input(mensaje))
    except:
        print('Este programa solo funciona con números!!')
        exit(1)

sql="insert into security_log(user_id, target_id, action, timestamp, ip_address) values (%s, %s,%s, %s, %s)"
target = get_float('Introduce target_id -> ')
action = input('introduce action -> ')
ip = input('introduce ip_address -> ')

datos=(1, 1, action, '2025-10-12', ip)
cursor1.execute(sql, datos)
conexion1.commit()

cursor1.execute("select * from security_log")
for tabla in cursor1:
    print(tabla)
conexion1.close()

conexion1.close()


'''

MariaDB [dvwa]> select * from security_log;
Empty set (0.048 sec)

MariaDB [dvwa]> describe security_log;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int(11)     | NO   | PRI | NULL    | auto_increment |
| user_id    | int(11)     | NO   | MUL | NULL    |                |
| target_id  | int(11)     | NO   | MUL | NULL    |                |
| action     | varchar(50) | NO   |     | NULL    |                |
| timestamp  | datetime    | NO   |     | NULL    |                |
| ip_address | varchar(45) | NO   |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
6 rows in set (0.005 sec)

MariaDB [dvwa]> ^C
MariaDB [dvwa]> select * from security_log;
+----+---------+-----------+---------+---------------------+------------+
| id | user_id | target_id | action  | timestamp           | ip_address |
+----+---------+-----------+---------+---------------------+------------+
|  1 |       1 |         1 | Ninguna | 2025-10-12 00:00:00 | 127.0.0.1  |
+----+---------+-----------+---------+---------------------+------------+
1 row in set (0.001 sec)

'''
