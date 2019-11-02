import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111"
	)

mycursor=mydb.cursor()
#create a database in MySQL named "mydatabase"
mycursor.execute("CREATE DATABASE mydatabase")
