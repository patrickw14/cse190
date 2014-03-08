import psycopg2
import sys
import random

#Define our connection string
conn_string = "host='localhost' dbname='CSE190' user='Postgres' password='test'"
 
# print the connection string we will use to connect
print ("Connecting to database ", conn_string, "")
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print ("Connected!\n")
    
#######################################################################################
filename = "first_names.txt"
file = open(filename, "r")
    
nameArray = []
    
for line in file:
    nameArray.append(line)
     
numName = len(nameArray)

roundNumber = 5  # number of friend per person

for i in range(0, numName):     # for each member
    fList = []      # Initialize the friend list
    
    for j in range(0, roundNumber):     # make (roundNumber) friends
        currFriend = random.randrange(0, numName)
        
        if(currFriend not in fList or currFriend != i):  # if already have this friend, run again
            cursor.execute("INSERT INTO friends VALUES ('" + str(i) + "', '" + str(currFriend) + "', NULL)")
        fList.append(currFriend)
            
###############################################################################################
conn.commit()

cursor.close()
conn.close()