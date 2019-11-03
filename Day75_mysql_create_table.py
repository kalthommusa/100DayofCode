import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="MyEmployee"
	)

mycursor=mydb.cursor()
#create a table in "mydatabase" named "Employee"
mycursor.execute("CREATE TABLE Employee(id INT AUTO_INCREMENT PRIMARY KEY,\
 FirstName VARCHAR(255), LastName VARCHAR(255), Age INT(11),\
 Gender VARCHAR(255), Salary INT(11) )")

