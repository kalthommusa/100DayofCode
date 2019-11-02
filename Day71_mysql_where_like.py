import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Select record(s) where the address is "Park Lane 38"
sql="SELECT * FROM customers WHERE address='Park Lane 38'"
#sql="SELECT * FROM customers WHERE address like '%way%'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)

