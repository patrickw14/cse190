import psycopg2
import sys
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

topicString = "topic0"
spawntopics = 10000
    
for i in range(1, spawntopics):
    topicString = topicString[:-1]
    topicString += str(i)
    cursor.execute("INSERT INTO topics VALUES ('" + str(i) + "', 'Some Topic')")
    
###############################################################################################
conn.commit()

cursor.close()
conn.close()