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

viewCount = 0

numPosts = 100000
numMember = 10000

random.seed(0xFE4432)
    
for post in range(0, numPosts):
    fList = []
    poster = ""
    
    cursor.execute("SELECT postedBy FROM posts WHERE id = '" + str(post) + "'")
    #poster = cursor.fecthone()  # poster id - from member
    
    for posterID in cursor:
        poster = posterID[0]
    
    cursor.execute("SELECT member2 FROM friends WHERE member1 = '" + str(poster) + "'")
    
    for friend in cursor:   # populating friend id for THIS Poster
        fList.append(friend[0])
    
    #--- CORRECT....!? ---#
        
    randNumReader = random.randrange(0, len(fList))     # deciding how many friends will read this post
    
    for iter in range(0,randNumReader):
        cursor.execute("INSERT INTO view VALUES ('" + str(viewCount) + "', NULL, '" + str(fList[iter]) + "', '" + str(post) + "')")
        viewCount += 1
    


                
###############################################################################################
conn.commit()

cursor.close()
conn.close()
