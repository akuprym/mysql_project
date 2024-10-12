import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# - select records where address contains "way":
# mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")

# - use placeholder %s to escape values:
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# - Order ascending:
#mycursor.execute("SELECT * FROM customers ORDER BY name")

# - Order descending:
# mycursor.execute("SELECT * FROM customers ORDER BY name DESC")


# - Delete:
# mycursor.execute("DELETE FROM customers WHERE address = 'Mountain 21'")
# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

sql = "DROP TABLE IF EXISTS clients"
mycursor.execute(sql)

# for x in myresult:
#    print(x)

