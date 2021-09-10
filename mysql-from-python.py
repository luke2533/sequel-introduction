import os
import datetime
import pymysql

# Get username from cloud9
#(modify varible if on another enviroment)

username = os.getenv("C9_USER")

#Conenct to the database
connection = pymysql.connect(host="localhost", user=username, password="", db="Chinook")

try:
    with connection.cursor() as cursor:
        # rows = [("Bob", 21, "1990-02-06 23:04:56"),
        #         ("Jim", 56, "1955-05-09 13:12:45"),
        #         ("Fred", 100, "1911-09-12 01:01:01")]
        # cursor.executemany("INSERT INTO Freinds VALUES (%s, %s, %s);", rows)
        # Inserts names
        list_of_names = ["Fred", "Fred"]
        format_strings = ",".join(["%s"]*len(list_of_names))
        cursor.execute("DELETE FROM Freinds WHERE name in ({})".format(format_strings), list_of_names)
        connection.commit()
finally:
    #Close the connection IMPORTANT
    connection.close()


# try:
#     with connection.cursor() as cursor:
        
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                         Freinds(name char(20), age int, DOB datetime);""")
       
# finally:
#     #Close the connection IMPORTANT
#     connection.close()
