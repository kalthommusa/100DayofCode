import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="MyEmployee"
	)

mycursor=mydb.cursor()
#Select all records from the "Employee" table, and display the result
sql="SELECT * FROM Employee"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)
#Select specific records from the "Employee" table, and display the result
sql="SELECT FirstName,Gender,Salary FROM Employee"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)
#Select all the records and sort the result alphabetically by FirstName (descending) 
sql="SELECT * FROM Employee ORDER BY FirstName DESC"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
	print(i)
#Delete any record where the Age is "34" 
sql="DELETE FROM Employee WHERE Age=34"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
