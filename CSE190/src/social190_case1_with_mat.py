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

startTime = time.time()

cursor.execute("SELECT readerID, friendID, (CAST(num_of_read AS float) / NULLIF(num_of_post,0)) AS ratio FROM (SELECT * FROM mat_view_case1 WHERE readerID = '" + str(givenMemberID) + "')t1 inner join mat_view_post1 t2 ON t1.friendID = t2.posterID")
#cursor.execute("SELECT (CAST(t1.num AS float) / NULLIF(t2.denom,0)) AS v FROM (SELECT SUM(num_of_read) AS num FROM mat_view_case1 WHERE readerID = '" + str(givenMemberID) + "' GROUP BY readerID)t1, (SELECT count(id) AS id FROM posts WHERE PostedBy = '" + str(poster) + "')t2")

endTime = time.time()
totalTime = endTime - startTime

for ratio in cursor:
    print("For readerID: " + str(ratio[0]) + " For friendID: " + str(ratio[1]) + " ratio: " + str(ratio[2]))
           
print ("Total time = " + str(totalTime))

###############################################################################################
conn.commit()

cursor.close()
conn.close()
