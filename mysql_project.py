import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwas74123",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 10")

mycursor.execute(sql, val)

mydb.commit() # This line is required to make the changes

print(mycursor.rowcount, "record inserted.")