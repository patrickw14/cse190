import psycopg2
import sys
import random
import name
from datetime import datetime


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

givenMemberID = 0  # Search target

nList = []
rList = []

startTime = datetime.now()

cursor.execute("SELECT .nation FROM member m, friends f WHERE f.member1 = '" + str(givenMemberID) + "' AND f.member2 = m.id")

for nation in cursor:
    nList.append(str(nation))


for nation in nList:
    cursor.execute("SELECT cast(t1.num AS float) / NULLIF(t2.denum, 0) FROM (SELECT SUM(num_of_read) AS NUM FROM mat_view_case2 WHERE ID  = '" + str(givenMemberID) + "' AND nation = '" + str(nation) + "' GROUP BY nation)t1, (SELECT SUM(num_ofpost) AS denum FROM mat_view_post2 m, friends f WHERE f.member1 = '" + str(givenMemberID) + "' AND f.member2 = p.posterID AND p.nation = '" + str(nation) + "' GROUP BY p.nation)t2")
    for ratio in cursor:
        rList.append(str(ratio))

endTime = datetime.now()
totalTime = endTime - startTime

for ratio in rList:
    print(str(ratio))
          
print ("Start time = " + str(startTime) + " End time = " + str(endTime) + " Total time = " + str(totalTime))

###############################################################################################
conn.commit()

cursor.close()
conn.close()
