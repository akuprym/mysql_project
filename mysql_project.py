import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwas74123",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

