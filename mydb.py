import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Blueshoe1'
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE WWM")
print("All Done!")