import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# - select records where address contains "way":
mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")

# - use placeholder %s to escape values:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2, ")
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

# - Order ascending:
mycursor.execute("SELECT * FROM customers ORDER BY name")

# - Order descending:
mycursor.execute("SELECT * FROM customers ORDER BY name DESC")

# - Delete:
mycursor.execute("DELETE FROM customers WHERE address = 'Mountain 21'")
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# - Delete table
sql = "DROP TABLE IF EXISTS clients"
mycursor.execute(sql)

# - Overwrite record:
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# - Use placeholder %s to escape values
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Return 5 records, start from position 3:
sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Join 2 tables
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

