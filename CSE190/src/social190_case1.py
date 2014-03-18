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

timelist = []
print "Query 1..."
rList = []
for givenMemberID in range(0, 10):  # Run for first 10 members in MEMBERS
    fList = []
    startTime = time.time()
    cursor.execute("SELECT member2 FROM friends WHERE member1 = '" + str(givenMemberID) + "'")

    for friend in cursor:
        #print("Current Friend id: " + str(friend[0]))
        fList.append(friend[0])
        #cursor.execute("SELECT id FROM posts WHERE postedBy = '" + str(friend[0]) + "'")
        
        '''
        for exist in cursor:
            fList.append(friend[0])
            print("post id: " + str(friend[0]))
            break
        '''
        
    for poster in fList:
        cursor.execute("SELECT (CAST(t1.id AS float) / NULLIF(t2.id,0)) AS v FROM (SELECT count(p.id) AS id FROM posts p, view v WHERE v.reader = '" + str(givenMemberID) + "' AND v.message = p.id AND p.postedBY = '" + str(poster) + "')t1, (SELECT count(id) AS id FROM posts WHERE PostedBy = '" + str(poster) + "')t2") 
        for ratio in cursor:
            if(ratio[0] != None):
                rList.append(ratio[0])

    endTime = time.time()
    totalTime = endTime - startTime
    timelist.append(totalTime)

timeSum = 0
for i in range(0, len(timelist)):
    timeSum += timelist[i]

for ratio in rList:
    print(str(ratio))

avgTime = timeSum / len(timelist)
print ("Average time: " + str(avgTime))
print ("Total time: " + str(timeSum))

###############################################################################################

conn.commit()

cursor.close()
conn.close()
