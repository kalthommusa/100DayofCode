import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Select all the records and sort the result alphabetically by name (ascending by default) 
sql="SELECT * FROM customers ORDER BY name"
"""
Select all the records and sort the result alphabetically by name (descending) 
sql="SELECT * FROM customers ORDER BY name DESC"
"""
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)