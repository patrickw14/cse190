import psycopg2
import sys
import random
import name

#Define our connection string
conn_string = "host='localhost' dbname='CSE190' user='" + name.getName() + "' password='test'"
 
# print the connection string we will use to connect
print ("Connecting to database ", conn_string, "")
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print ("Connected!\n")
    
#######################################################################################

cursor.execute("DELETE FROM view;")
cursor.execute("DELETE FROM posts;")
cursor.execute("DELETE FROM topics;")
cursor.execute("DELETE FROM friends;")
cursor.execute("DELETE FROM member;")

###############################################################################################
conn.commit()

cursor.close()
conn.close()