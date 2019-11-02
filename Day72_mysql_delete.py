import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Delete any record where the address is "Highway 21" 
sql="DELETE FROM customers WHERE address='Highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
