import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='deliverycenter',
                                         user='root',
                                         password='root',
                                         port='3308')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print('Connected to MYSQL Server Version: ', db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print('You are connected to database: ', record)

except Error as e:
    print('Error while connecting to MYSQL', e)

