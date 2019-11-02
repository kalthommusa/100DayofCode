import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#create a table in "mydatabase" named "customers"
mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY,\
 name VARCHAR(255), address VARCHAR(255))")
