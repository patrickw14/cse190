import psycopg2
import sys
import random

#Define our connection string
conn_string = "host='localhost' dbname='CSE190' user='Postgres' password='test'"
 
# print the connection string we will use to connect
print ("Connecting to database ", conn_string, "")
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print ("Connected!\n")
    
#######################################################################################

filename = "first_names.txt"
file = open(filename, "r")
    
nameArray = []
    
for line in file:
    nameArray.append(line)
       
filename = "nations.txt"
file = open(filename, 'r')
    
m_id = 0
    
nationArray = []
nationNumber = 195 # there are 195 nations in the list
    
for line in file:
    nationArray.append(line)
    
#cursor.execute("INSERT INTO member VALUES('5', 'name1', 'nation1', 'NULL', 'NULL')")
    
for name in nameArray:
    insertNation = nationArray[random.randrange(1,nationNumber)]
    cursor.execute("INSERT INTO member VALUES ('" + str(m_id) + "', '" + name + "', '" + insertNation + "', NULL, NULL)")
    m_id = m_id + 1
    
###############################################################################################
conn.commit()

cursor.close()
conn.close()