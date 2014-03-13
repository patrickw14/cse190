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
cursor.execute("CREATE OR REPLACE FUNCTION add_to_post_fn() RETURNS trigger AS $addtopost$ BEGIN INSERT INTO mat_view_post1 (posterID, num_of_post) SELECT NEW.id, 0; INSERT INTO mat_view_post2 (posterID, nation, num_of_post) SELECT NEW.id, m.nation, 0 FROM NEW, member WHERE NEW.id = m.id; RETURN NEW; END $addtopost$ LANGUAGE 'plpgsql';")
cursor.execute("CREATE TRIGGER add_to_post AFTER INSERT ON member FOR EACH ROW EXECUTE PROCEDURE add_to_post_fn();")

# TRIGGER THAT WILL INCREMENT EACH PERSON'S POST COUNT WHENEVER THE POST IS ADDED.
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE OR REPLACE FUNCTION inc_post_fn() RETURNS trigger AS $incrementpost$ BEGIN UPDATE mat_view_post1 SET num_of_post = num_of_post+1 FROM mat_view_post1 m, posts p WHERE m.posterID = NEW.postedBy; UPDATE mat_view_post1 SET num_of_post = num_of_post+1 FROM mat_view_post1 m, posts p WHERE m.posterID = NEW.postedBy; RETURN NEW; END $incrementpost$ LANGUAGE 'plpgsql';")
cursor.execute("CREATE TRIGGER inc_post AFTER INSERT ON posts FOR EACH ROW EXECUTE PROCEDURE inc_post_fn();")

# TRIGGERS THAT WILL ADD FRIEND ROW TO EACH VIEW CASES WHENEVER A FRIEND IS ADDED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE OR REPLACE FUNCTION add_to_case_fn() RETURNS trigger AS $addtocase$ BEGIN INSERT INTO mat_view_case1 (readerid, friendid, num_of_read) SELECT NEW.member1, NEW.member2, 0 FROM NEW, member; INSERT INTO mat_view_case2 (readerid, friendid, nation, num_of_read) SELECT NEW.member1, NEW.member2, m.nation, 0 FROM NEW, member WHERE NEW.member2 = m.id; RETURN NEW; END $addtocase$ LANGUAGE 'plpgsql';")
cursor.execute("CREATE TRIGGER add_to_case AFTER INSERT ON friends FOR EACH ROW EXECUTE PROCEDURE add_to_case_fn();")


# TRIGGERS THAT WILL UPDATE THE TABLES WHEN A VIEW IS CREATED
# CURRENTLY DOESN"T WORK BECAUSE OF SYNTAX ERROR
cursor.execute("CREATE OR REPLACE FUNCTION inc_case_fn() RETURNS trigger AS $incrementcase$ BEGIN UPDATE mat_view_case1 SET num_of_post = num_of_post+1 FROM mat_view_post1 m, posts p WHERE m.posterID = NEW.postedBy; UPDATE mat_view_post2 SET num_of_post = num_of_post+1 FROM mat_view_post2 m, posts p WHERE m.posterID = NEW.postedBy; RETURN NEW; END $incrementpost$ LANGUAGE 'plpgsql';")
cursor.execute("CREATE TRIGGER inc_case AFTER INSERT ON view FOR EACH ROW EXECUTE PROCEDURE inc_case_fn();")

print("Trigger Creation is completed")
###############################################################################################
conn.commit()

cursor.close()
conn.close()