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
#cursor.execute("ALTER TABLE member DISABLE TRIGGER add_to_post")
#conn.commit()

########################################################################################

filename = "first_names.txt"
file = open(filename, "r")

numName = 2000 #break point to limit the size of the table
totalTime = 0;
    
random.seed(0xFE4432)    
    
nameArray = []
    
for line in file:
    nameArray.append(line)
       
filename = "nations.txt"
file = open(filename, 'r')
    
m_id = 0
    
nationArray = []
nationNumber = 195 # there are 195 nations in the list
    
for line in file:
    nationArray.append(line)
    
#cursor.execute("INSERT INTO member VALUES('5', 'name1', 'nation1', 'NULL', 'NULL')")

for name in nameArray:
    if(m_id == numName):
        break
    insertNation = nationArray[random.randrange(1,nationNumber)]
    
    startTime = time.time()
    
    cursor.execute("INSERT INTO member VALUES ('" + str(m_id) + "', '" + name + "', '" + insertNation + "', NULL, NULL)")
    conn.commit()
    
    endTime = time.time()
    totalTime = totalTime + (endTime - startTime)
    
    m_id = m_id + 1
    
###############################################################################################
conn.commit()

print("Time taken: " + str(totalTime))

# Re-enabling the trigger temporarily. Comment if not neeeded
#cursor.execute("ALTER TABLE member DISABLE TRIGGER add_to_post")
#conn.commit()

########################################################################################

cursor.close()
conn.close()