import mysql.connector
#create a connection to MySQL server
mydb=mysql.connector.connect(
    host="127.0.0.1",
	user="root",
	passwd="pass111",
	database="mydatabase"
	)

mycursor=mydb.cursor()
#Insert multiple rows/records and fill the "customers" table with data
sql="INSERT INTO customers(name, address) VALUES(%s,%s)"
val=[
   ("Kalthom","Al-Mansor st"),
   ("Hannah","Park Lane 38"),
   ("John","Highway 21"),
   ("Susan","Sideway 633"),
   ("Ben","Valley 75")
]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")