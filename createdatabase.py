#this is python file from W3Schools python training for creating database using python.
import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        username="root",
        password='pass'
        )

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE myDatabase")
