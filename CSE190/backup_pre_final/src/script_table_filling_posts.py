import psycopg2
import sys
import random
import name
import time


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

# Disabling the trigger temporarily. Comment if not neeeded
#cursor.execute("ALTER TABLE posts DISABLE TRIGGER inc_post")
#conn.commit()

########################################################################################

numPosts = 10000
numMember = 1000
numTopic = 10000

random.seed(0xFE4432)

startTime = time.time()
    
for i in range(0, numPosts): 
    randTopic = random.randrange(1, numTopic)
    randPoster = random.randrange(0, numMember)   # we use the id not name.
    cursor.execute("INSERT INTO posts VALUES ('" + str(i) + "', '" + str(randPoster) + "', 'Random Title', 'This is text body', NULL, '" + str(randTopic) + "')" )
           
###############################################################################################
conn.commit()

endTime = time.time()
totalTime = endTime - startTime

print("Time taken: " + str(totalTime))

# Re-enabling the trigger temporarily. Comment if not neeeded
#cursor.execute("ALTER TABLE posts DISABLE TRIGGER inc_post")
#conn.commit()

########################################################################################

cursor.close()
conn.close()
