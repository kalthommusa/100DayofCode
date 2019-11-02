import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
"""
Select the 3 first records in the "customers" table
sql="SELECT * FROM customers LIMIT 3"
"""
#Start from position 3, and return 2 records
sql="SELECT * FROM customers LIMIT 2 OFFSET 2"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)
