import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwas74123",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN(id INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)