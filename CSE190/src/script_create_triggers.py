import psycopg2
import sys
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

Following codes do not work yet because of postgres syntax error; postgres syntax is apparently a lot different from MS SQL syntax

# TRIGGER THAT WILL ADD EACH PERSON'S POST COUNT WHENEVER THE PERSON IS ADDED.
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE TRIGGER add_to_post AFTER INSERT ON member AS BEGIN INSERT INTO mat_view_post (posterID, num_of_post) (SELECT id, 0 FROM  NEW) END")

# TRIGGER THAT WILL INCREMENT EACH PERSON'S POST COUNT WHENEVER THE POST IS ADDED.
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE TRIGGER inc_post AFTER INSERT ON posts AS BEGIN UPDATE mat_view_post SET num_of_post = num_of_post + 1 FROM mat_view_post m, NEW n WHERE m.readerID = n.readerID END")

# TRIGGERS THAT WILL ADD FRIEND ROW TO EACH VIEW CASES WHENEVER A FRIEND IS ADDED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE TRIGGER add_friend AFTER INSERT ON friends AS BEGIN INSERT INTO mat_view_case1(readerID, friendID, num_of_read) (SELECT member1, member2, 0 FROM NEW); INSERT INTO mat_view_case2(readerID, nation, num_of_read) (SELECT f.member1, m.nation, 0 FROM NEW n, friends f, members m WHERE n.member1 = f.member1 AND f.member2 = m.id) END")

# TRIGGERS THAT WILL UPDATE THE TABLES WHEN A VIEW IS CREATED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE TRIGGER inc_view AFTER INSERT ON view AS BEGIN UPDATE mat_view_case1 SET num_of_read = num_of_read + 1 FROM mat_view_case1 m, NEW n, posts p WHERE m.ID = n.reader AND n.message = p.id AND p.postedBy = m.friendID; UPDATE mat_view_case2 SET num_of_read = num_of_read + 1 FROM mat_view_case2 m, NEW n, posts p, member mb WHERE m.ID = n.reader AND n.message = p.id AND p.postedBy = m.friendID AND m.friendID = mb.id AND mb.nation = m.nation END")

print("Trigger Creation is completed")
###############################################################################################
conn.commit()

cursor.close()
conn.close()