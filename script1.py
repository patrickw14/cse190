import psycopg2

conn = psycopg2.connect("dbname=CSE190 user=postgres password=test")

cur = conn.cursor()

cur.execute("CREATE TABLE member (id INT NOT NULL PRIMARY KEY, name VARCHAR(30), nation VARCHAR(30), birthday VARCHAR(10), time_stamp VARCHAR(30));")
cur.execute("CREATE TABLE friends (member1 INT NOT NULL, member2 INT NOT NULL, time_stamp VARCHAR(30), PRIMARY KEY (member1, member2), FOREIGN KEY (member1) REFERENCES member, FOREIGN KEY (member2) REFERENCES member);")
cur.execute("CREATE TABLE topics (id INT NOT NULL PRIMARY KEY, name VARCHAR(30));")
cur.execute("CREATE TABLE posts (id INT NOT NULL PRIMARY KEY, postedBy INT NOT NULL, title VARCHAR(30), textBody VARCHAR(150), time_stamp VARCHAR(15), topic INT NOT NULL, FOREIGN KEY (postedBy) REFERENCES member, FOREIGN KEY (topic) REFERENCES topics);")
cur.execute("CREATE TABLE view (id INT NOT NULL PRIMARY KEY, time_stamp VARCHAR(30), reader INT NOT NULL, message INT NOT NULL, FOREIGN KEY (reader) REFERENCES member, FOREIGN KEY (message) REFERENCES posts);")

