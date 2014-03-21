import psycopg2
import name


print("Working?")
 
#Define our connection string
conn_string = "host='localhost' dbname='CSE190' user='" + name.getName() + "' password='test'"
 
# print the connection string we will use to connect
print ("Connecting to database ", conn_string)
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print ("Connected!")


cursor.execute("CREATE TABLE member (id INT NOT NULL PRIMARY KEY, name VARCHAR(30), nation VARCHAR(30), birthday VARCHAR(10), time_stamp VARCHAR(30));")
cursor.execute("CREATE TABLE friends (member1 INT NOT NULL, member2 INT NOT NULL, time_stamp VARCHAR(30), PRIMARY KEY (member1, member2), FOREIGN KEY (member1) REFERENCES member, FOREIGN KEY (member2) REFERENCES member);")
cursor.execute("CREATE TABLE topics (id INT NOT NULL PRIMARY KEY, name VARCHAR(30));")
cursor.execute("CREATE TABLE posts (id INT NOT NULL PRIMARY KEY, postedBy INT NOT NULL, title VARCHAR(30), textBody VARCHAR(150), time_stamp VARCHAR(15), topic INT NOT NULL, FOREIGN KEY (postedBy) REFERENCES member, FOREIGN KEY (topic) REFERENCES topics);")
cursor.execute("CREATE TABLE view (id INT NOT NULL PRIMARY KEY, time_stamp VARCHAR(30), reader INT NOT NULL, message INT NOT NULL, FOREIGN KEY (reader) REFERENCES member, FOREIGN KEY (message) REFERENCES posts);")

print("Execution Finished.")

#FOR CHECKING PURPOSE
cursor.execute('SELECT * FROM member LIMIT 100')

row_count = 0
for row in cursor:
    row_count += 1
    print ("ROW: ", row_count, " NAME: ", row)   

conn.commit()

cursor.close()
conn.close()