import psycopg2
import sys
import random
import name


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

fList = []
rList = []

cursor.execute("SELECT member2 FROM friends WHERE member1 = '" + str(givenMemberID) + "'")

for friend in cursor:
    cursor.execute("SELECT id FROM posts WHERE postedBy = '" + str(friend[0]) + "'")
    for exist in cursor:
        fList.append(friend[0])
        print("Friend id: " + str(friend[0]))
        break
    
for poster in fList:
    cursor.execute("SELECT (CAST(t1.id AS float) / t2.id) AS v FROM (SELECT count(p.id) AS id FROM posts p, view v WHERE v.reader = '" + str(givenMemberID) + "' AND v.message = p.id AND p.postedBY = '" + str(poster) + "')t1, (SELECT count(id) AS id FROM posts WHERE PostedBy = '" + str(poster) + "')t2") 
    for ratio in cursor:
        rList.append(ratio[0])

for ratio in rList:
    print(str(ratio))
                
###############################################################################################
conn.commit()

cursor.close()
conn.close()
