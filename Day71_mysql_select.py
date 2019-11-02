import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Select all records from the "customers" table, and display the result
sql="SELECT * FROM customers"
#sql="SELECT name,address FROM customers"
mycursor.execute(sql)
myresult=mycursor.fetchall()
#myresult=mycursor.fetchone()
#print(myresult)
for i in myresult:
	print(i)
