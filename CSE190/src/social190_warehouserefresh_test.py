import psycopg2
import sys
import random
import name
import time

insertedRowsSinceLastQuery = 0
insertQueue = []



#######################################################################################

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
totalMembers = 1000
totalPosts = 10000

def executeInsertRows():
    global insertQueue
    for command in insertQueue:
        cursor.execute(command)
    insertQueue = []


def insertRow(insertCommand):
    global insertedRowsSinceLastQuery
    if insertedRowsSinceLastQuery > 30:
        executeInsertRows()
        insertedRowsSinceLastQuery = 0
    insertQueue.append(insertCommand)
    insertedRowsSinceLastQuery = insertedRowsSinceLastQuery + 1

def executeQuery(memberID, friendList):
    global insertedRowsSinceLastQuery
    if insertedRowsSinceLastQuery != 0:
        executeInsertRows()
        insertedRowsSinceLastQuery = 0
    for poster in friendList:
        cursor.execute("SELECT (CAST(num_of_read AS float) / NULLIF(num_of_post,0)) AS v FROM (SELECT * FROM mat_view_case1 WHERE readerID = '" + str(memberID) + "')t1 inner join mat_view_post1 t2 ON t1.friendID = t2.posterID")


def insertPost():
    global totalPosts
    randTopic = random.randrange(1, 10000)
    randPoster = random.randrange(0, totalMembers)
    insertRow("INSERT INTO posts VALUES ('" + str(totalPosts) + "', '" + str(randPoster) + "', 'Random Title', 'This is text body', NULL, '" + str(randTopic) + "')")
    insertRow("UPDATE mat_view_post1 SET num_of_post = num_of_post+1 WHERE posterID = " + str(randPoster))
    insertRow("UPDATE mat_view_post2 SET num_of_post = num_of_post+1 WHERE posterID = " + str(randPoster))

def insertMember():
    global totalMembers
    insertRow("INSERT INTO member VALUES ('" + str(totalMembers) + "', 'John', 'USA', NULL, NULL)")
    insertRow("INSERT INTO mat_view_post1 VALUES ('" + str(totalMembers) + "', '0')")
    insertRow("INSERT INTO mat_view_post2 VALUES ('" + str(totalMembers) + "', 'USA', '0')")

inserttimelist = []
querytimelist = []
timelist = []

action = "INSERT"
random.seed(0xFE4432)

for i in range(0, 1000):
    #print str(i) + " " + action + "..."
    fList = []
    rList = []
    if action == "INSERT":
        insertType = random.randrange(0,2)
        startTime = time.time()
        if insertType == 0:
            insertMember()
            totalMembers = totalMembers + 1
        elif insertType == 1:
            insertPost()
            totalPosts = totalPosts + 1
        endTime = time.time()
        totalTime = endTime - startTime
        inserttimelist.append(totalTime)
        timelist.append(totalTime)

    elif action == "QUERY":
        fList = []
        givenMemberID = random.randrange(0, 1000)
        startTime = time.time()
        cursor.execute("SELECT member2 FROM friends WHERE member1 = '" + str(givenMemberID) + "'")
        for friend in cursor:
            fList.append(friend[0])

        executeQuery(givenMemberID, fList)
        endTime = time.time()
        totalTime = endTime - startTime
        querytimelist.append(totalTime)
        timelist.append(totalTime)

    newAction = random.randrange(0, 5)
    if newAction < 0:
        action = "INSERT"
    else:
        action = "QUERY"

insertTimeSum = 0
for i in range(0, len(inserttimelist)):
    insertTimeSum += inserttimelist[i]

queryTimeSum = 0
for i in range(0, len(querytimelist)):
    queryTimeSum += querytimelist[i]

print "Over " + str(len(inserttimelist)) + " inserts, Average insert time: " + str(insertTimeSum / len(inserttimelist))
print "Over " + str(len(querytimelist)) + " queries, Average query time: " + str(queryTimeSum / len(querytimelist))


###############################################################################################

#conn.commit()

cursor.close()
conn.close()