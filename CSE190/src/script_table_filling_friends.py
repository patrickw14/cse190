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

numName = 10000

roundNumber = 30  # number of friend per person

random.seed(0xFE4432)

for i in range(0, numName):     # for each member
    fList = []      # Initialize the friend list
    
    for j in range(0, roundNumber):     # make (roundNumber) friends
        currFriend = random.randrange(0, numName)   # we use the id not name.
        
        if(currFriend not in fList and currFriend != i and currFriend > i):  # if already have this friend, run again
            cursor.execute("INSERT INTO friends VALUES ('" + str(i) + "', '" + str(currFriend) + "', NULL)")
            cursor.execute("INSERT INTO friends VALUES ('" + str(currFriend) + "', '" + str(i) + "', NULL)")
            
            '''
            try:
                cursor.execute("INSERT INTO friends VALUES ('" + str(currFriend) + "', '" + str(i) + "', NULL)")
            except:
                print("")
            '''
            
            fList.append(currFriend)
            
###############################################################################################
conn.commit()

cursor.close()
conn.close()
