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

# CREATING EACH PERSON'S POST COUNT MATERIALIZE VIEW
cursor.execute("CREATE TABLE mat_view_post1 (posterID int NOT NULL, num_of_post int NOT NULL, PRIMARY KEY (posterID), FOREIGN KEY (posterID) REFERENCES member)")
cursor.execute("CREATE INDEX mat_view_post1_index ON mat_view_post1 (posterID)")

# CREATING MATERIALIZE VIEW THAT HAS A PERSON, HIS FRIENDS AND # OF POSTS HE READ FROM THAT PERSON
cursor.execute("CREATE TABLE mat_view_case1 (readerID int NOT NULL, friendID int NOT NULL, num_of_read int NOT NULL, PRIMARY KEY (readerID, friendID, num_of_read), FOREIGN KEY (readerID) REFERENCES member, FOREIGN KEY (friendID) REFERENCES member)")
cursor.execute("CREATE INDEX mat_view_case1_index ON mat_view_case1 (readerID)")


### QUERY 2 ###
# CREATING EACH PERSON'S POST COUNT MATERIALIZE VIEW
cursor.execute("CREATE TABLE mat_view_post2 (posterID int NOT NULL, nation varchar(30), num_of_post int NOT NULL, PRIMARY KEY (posterID), FOREIGN KEY (posterID) REFERENCES member)")
cursor.execute("CREATE INDEX mat_view_post2_index ON mat_view_post2 (posterID)")

# CREATING MATERIALIZE VIEW THAT HAS A PERSON, HIS FRIENDS, EACH FRIENDS NATION, AND # OF POSTS HE READ FROM THAT PERSON
cursor.execute("CREATE TABLE mat_view_case2 (readerID int NOT NULL, friendID int NOT NULL, nation varchar(30), num_of_read int NOT NULL, PRIMARY KEY (readerID, friendID), FOREIGN KEY (readerID) REFERENCES member, FOREIGN KEY (friendID) REFERENCES member)")
cursor.execute("CREATE INDEX mat_view_case2_index ON mat_view_case2 (readerID)")

print("Materialize View Creation is completed")
###############################################################################################
conn.commit()

cursor.close()
conn.close()