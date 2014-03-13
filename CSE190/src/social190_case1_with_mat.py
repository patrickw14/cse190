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

rList = []

startTime = datetime.now()

cursor.execute("SELECT num_of_read, num_of_post FROM (mat_view_case1) natural join (mat_view_post)")

for tuple in cursor:
    rList.append(float(tuple[0]) / float(tuple[1]))

endTime = datetime.now()
totalTime = endTime - startTime

for ratio in rList:
    print(str(ratio))
          
print ("Start time = " + str(startTime) + " End time = " + str(endTime) + " Total time = " + str(totalTime))

###############################################################################################
conn.commit()

cursor.close()
conn.close()
