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

# Following codes do not work yet because of postgres syntax error; postgres syntax is 
# apparently a lot different from MS SQL syntax

# TRIGGER THAT WILL ADD EACH PERSON'S POST COUNT WHENEVER THE PERSON IS ADDED.
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("DROP TRIGGER add_to_post ON member")

# TRIGGER THAT WILL INCREMENT EACH PERSON'S POST COUNT WHENEVER THE POST IS ADDED.
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("DROP TRIGGER inc_post ON posts")

# TRIGGERS THAT WILL ADD FRIEND ROW TO EACH VIEW CASES WHENEVER A FRIEND IS ADDED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("DROP TRIGGER add_to_case ON friends")

# TRIGGERS THAT WILL UPDATE THE TABLES WHEN A VIEW IS CREATED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("DROP TRIGGER inc_case ON view")

print("Trigger Deletion is completed")
###############################################################################################
conn.commit()

cursor.close()
conn.close()