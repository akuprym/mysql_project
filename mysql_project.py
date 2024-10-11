import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(name VARCHAR (225), address VARCHAR (225))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)