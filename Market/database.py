import mysql.connector



conn =  mysql.connector.connect(host="localhost",user= "root", passwd="342516", port = "3307")
my_cursor = conn.cursor()
my_cursor.execute("CREATE DATABASE market")