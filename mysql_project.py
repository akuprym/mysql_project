import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwas74123",
    database="mydatabase"
)

mycursor = mydb.cursor()

# select records where address contains "way":
# mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

