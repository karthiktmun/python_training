import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        username="root",
        password="pass"
        )

mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
[root@localhos
