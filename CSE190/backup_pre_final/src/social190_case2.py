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

filename = "nations.txt"
file = open(filename, 'r')

nationArray = []
nationNumber = 195 # there are 195 nations in the list

rList = []
tList = []

for line in file:
    nationArray.append(line)

startTime = time.time()
for nation in nationArray:
    cursor.execute("SELECT (CAST(t1.c AS float) / NULLIF(t2.c, 0)) AS v FROM (SELECT count(*) AS c FROM member m, friends f, posts p, view v WHERE v.reader = '" + str(givenMemberID) + "' AND v.message = p.id AND f.member1 = v.reader AND f.member2 = p.postedBy AND f.member2 = m.id AND m.nation = '" + nation + "')t1, (SELECT count(*) AS c FROM member m, friends f, posts p WHERE f.member1 = '" + str(givenMemberID) + "' AND f.member2 = p.postedBy AND p.postedBy = m.id AND m.nation = '" + nation +"')t2")
    for ratio in cursor:
        if(ratio[0] != None):
            rList.append(ratio[0])
            tList.append(nation)

endTime = time.time()
totalTime = endTime - startTime

count = 0

for ratio in rList:
    print("For nation: " + str(tList[count]) + " ratio: " + str(ratio))
    count = count + 1
 
print ("Start time = " + str(startTime) + " End time = " + str(endTime) + " Total time = " + str(totalTime))
                
###############################################################################################
conn.commit()

cursor.close()
conn.close()
