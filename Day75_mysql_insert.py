import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="MyEmployee"
	)

mycursor=mydb.cursor()
#Insert multiple rows/records and fill the "Employee" table with data
sql="INSERT INTO Employee(FirstName, LastName, Age, Gender, Salary) VALUES(%s,%s,%s,%s,%s)"
val=[
   ("Ahmed","Ali", 30, "Male", 10000),
   ("Khalid","Muhammad", 34, "Male", 7000),
   ("Norah","Saleh", 29, "Female", 7000)
]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")