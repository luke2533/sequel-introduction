import os
import pymysql

# Get username from cloud9
#(modify varible if on another enviroment)

username = os.getenv("C9_USER")

#Conenct to the database
connection = pymysql.connect(host="localhost", user=username, password="", db="Chinook")

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection IMPORTANT
    connection.close()