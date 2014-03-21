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

givenMemberID = 2; # the person to search for

query = "SELECT t1.reader, t1.postedBy, t1.readCount, t2.postCount, (CAST(t1.readCount AS float) / NULLIF(t2.postCount,0)) AS ratio FROM (    SELECT v.reader, p.postedBy, count(*) AS readCount FROM view v, posts p WHERE p.id = v.message AND v.reader = '" + str(givenMemberID) + "' GROUP BY v.reader, p.postedBy ORDER BY postedBy)t1 LEFT JOIN(    SELECT postedBy, count(*) AS postCount FROM posts GROUP BY postedBy ORDER BY postedBy)t2 ON t1.postedBy = t2.postedBy"

startTime = time.time()

cursor.execute(query)

endTime = time.time()

totalTime = endTime - startTime

for tuple in cursor:
    print("For friendID" + str(tuple[1]) + " ratio: " + str(tuple[4]))
    
print ("Total time: " + str(totalTime))

###############################################################################################

conn.commit()

cursor.close()
conn.close()
