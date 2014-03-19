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

totalTime = 0
nList = []
rList = []
tList = []

cursor.execute("SELECT m.nation FROM member m, friends f WHERE f.member1 = '" + str(givenMemberID) + "' AND f.member2 = m.id")

for nation in cursor:
    nList.append(str(nation[0]))

for nation in nList:
    
    startTime = time.time()
    
    cursor.execute("SELECT cast(t1.num AS float) / NULLIF(t2.denum, 0) FROM (SELECT SUM(num_of_read) AS NUM FROM mat_view_case2 WHERE readerID  = '" + str(givenMemberID) + "' AND nation = '" + nation + "' GROUP BY nation)t1, (SELECT SUM(num_of_post) AS denum FROM mat_view_post2 m, friends f WHERE f.member1 = '" + str(givenMemberID) + "' AND f.member2 = m.posterID AND m.nation = '" + nation + "' GROUP BY m.nation)t2")
    
    endTime = time.time()
    totalTime = totalTime + (endTime - startTime)
    
    for ratio in cursor:
        rList.append(str(ratio[0]))
        tList.append(nation)

count = 0

for ratio in rList:
    print("For nation: " + str(tList[count]) + " ratio: " + str(ratio))
    count = count + 1
          
print ("Start time = " + str(startTime) + " End time = " + str(endTime) + " Total time = " + str(totalTime))

###############################################################################################
conn.commit()

cursor.close()
conn.close()
