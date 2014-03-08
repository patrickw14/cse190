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

numPosts = 100000
numMember = 10000
numTopic = 10000

random.seed(0xFE4432)
    
for i in range(0, numPosts):
    randTopic = random.randrange(1, numTopic)
    randPoster = random.randrange(0, numMember)   # we use the id not name.
    cursor.execute("INSERT INTO posts VALUES ('" + str(i) + "', '" + str(randPoster) + "', 'Random Title', 'This is text body', NULL, '" + str(randTopic) + "')" )
                
###############################################################################################
conn.commit()

cursor.close()
conn.close()
