import psycopg2
import sys
import random

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='CSE190' user='postgres'" # password='test'"
 
    # print the connection string we will use to connect
    print ("Connecting to database ", conn_string, "")
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print ("Connected!\n")
    
    #######################################################################################

    filename = "first_names.txt"
    file = open(filename, "r")
    
    nameArray = []
    
    for line in file:
        nameArray.append(line)
        
    filename = "nations.txt"
    file = open(filename, 'r')
    
    nationArray = []
    nationNumber = 195 # there are 195 nations in the list
    
    for line in file:
        nationArray.append(line)
    
    for name in nameArray:
        insertNation = nationArray[random.randrange(1,nationNumber+1)]
        cursor.execute("INSERT INTO members VALUES ", name, ", ", insertNation, ", NULL, NULL")
    
    ###############################################################################################
