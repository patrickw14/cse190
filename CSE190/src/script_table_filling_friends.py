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

# Disabling the trigger temporarily. Comment if not neeeded
#cursor.execute("ALTER TABLE friends DISABLE TRIGGER add_to_case")
#conn.commit()

########################################################################################

numName = 2000

roundNumber = 50  # number of friend per person

random.seed(0xFE4432)

totalTime = 0

for i in range(0, numName):     # for each member
    fList = []      # Initialize the friend list
    
    for j in range(0, roundNumber):     # make (roundNumber) friends
        currFriend = random.randrange(0, numName)   # we use the id not name.
        
        if(currFriend not in fList and currFriend != i and currFriend > i):  # if already have this friend, run again
            startTime = time.time()
            
            cursor.execute("INSERT INTO friends VALUES ('" + str(i) + "', '" + str(currFriend) + "', NULL)")
            conn.commit()
            cursor.execute("INSERT INTO friends VALUES ('" + str(currFriend) + "', '" + str(i) + "', NULL)")
            conn.commit()
            
            endTime = time.time()
            totalTime = totalTime + (endTime - startTime)
            '''
            try:
                cursor.execute("INSERT INTO friends VALUES ('" + str(currFriend) + "', '" + str(i) + "', NULL)")
            except:
                print("")
            '''
            
            fList.append(currFriend)
            
###############################################################################################
conn.commit()

print("Time taken: " + str(totalTime))


# Re-enabling the trigger temporarily. Comment if not neeeded
#cursor.execute("ALTER TABLE friends DISABLE TRIGGER add_to_case")
#conn.commit()

########################################################################################

cursor.close()
conn.close()
