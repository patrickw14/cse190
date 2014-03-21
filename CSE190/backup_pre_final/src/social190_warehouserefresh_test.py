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
    for command in insertQueue:
        cursor.execute(command)
        

def insertRow(insertCommand):
    if insertedRowsSinceLastQuery > 30:
        executeInsertRows()
        insertedRowsSinceLastQuery = 0
    else:
        insertQueue.append(insertCommand)
        insertedRowsSinceLastQuery++

def executeQuery(memberID, friendList):
    if insertedRowsSinceLastQuery != 0:
        executeInsertRows()
    for poster in friendList:
        #fill in query
        cursor.execute("")


def insertPost():
    randTopic = random.randrange(1, 10000)
    randPoster = random.randrange(0, totalMembers)
    insertRow("INSERT INTO posts VALUES ('" + str(totalPosts) + "', '" + str(randPoster) + "', 'Random Title', 'This is text body', NULL, '" + str(randTopic) + "')")
    insertRow("UPDATE mat_view_post1 SET num_of_post = num_of_post+1 WHERE posterID = " + str(randPoster))
    insertRow("UPDATE mat_view_post2 SET num_of_post = num_of_post+1 WHERE posterID = " + str(randPoster))
    totalPosts++

def insertMember():
    insertRow("INSERT INTO member VALUES ('" + str(totalMembers) + "', 'John', 'USA', NULL, NULL)")
    insertRow("INSERT INTO mat_view_post1 VALUES (' + str(totalMembers) + ', 0)")
    insertRow("INSERT INTO mat_view_post2 VALUES ('" + str(totalMembers) + "', 'USA', 0)")
    totalMembers++

inserttimelist = []
querytimelist = []

action = "INSERT"
random.seed(0xFE4432)

for i in range(0, 300):
    print str(i) + " " + action "..."
    fList = []
    rList = []
    if action == "INSERT":
        insertType = random.randrange(0,2)
        startTime = time.time()
        if insertType == 0:
            insertMember()
        elif insertType == 1:
            insertPost()
        endTime = time.time()
        totalTime = endTime - startTime
        inserttimelist.append(totalTime)

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

    newAction = random.randrange(0, 5)
    if newAction < 4:
        action = "INSERT"
    else:
        action = "QUERY"

insertTimeSum = 0
for i in range(0, len(inserttimelist)):
    insertTimeSum += inserttimelist[i]

queryTimeSum = 0
for i in range(0, len(querytimelist)):
    queryTimeSum += querytimelist[i]

print "Average insert time: " + str(insertTimeSum / len(inserttimelist))
print "Average query time: " + str(queryTimeSum / len(querytimelist))


###############################################################################################

conn.commit()

cursor.close()
conn.close()
