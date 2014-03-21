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

givenMemberID = 2  # Search target

query = "SELECT t1.readerID, t2.nation, SUM(t1.num_of_read) AS totalRead, SUM(t2.num_of_post) AS totalPosted, (CAST(SUM(t1.num_of_read) AS float) / NULLIF(SUM(t2.num_of_post),0)) AS ratio FROM (    SELECT * FROM mat_view_case2 WHERE readerID = '" + str(givenMemberID) + "')t1 LEFT JOIN (    SELECT * FROM mat_view_post2)t2 ON t2.posterID = t1.friendID GROUP BY t1.readerID, t2.nation"

startTime = time.time()

cursor.execute(query)

endTime = time.time()
totalTime = endTime - startTime

for ratio in cursor:
    print("For readerID: " + str(ratio[0]) + " For nation: " + str(ratio[1]) + " ratio: " + str(ratio[4]))
          
print ("Total time = " + str(totalTime))

###############################################################################################
conn.commit()

cursor.close()
conn.close()
