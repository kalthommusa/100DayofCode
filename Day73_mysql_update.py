import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Update and overwrite the address column from "Valley 345" to "Mountain 19"
sql="UPDATE customers SET address='Mountain 19' WHERE address='Valley 75'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) updated")
