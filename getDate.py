#!/usr/bin/python
import MySQLdb
from datetime import timedelta, datetime

# Initialize the Database
conn = MySQLdb.connect(host='localhost',user='root' , passwd='qwer1234',db='twitter')
cursor = conn.cursor()

N = 1000;   #number of different user
T = 40;   #steps in time series
# Get users
users = []
fp = file('users.txt')
for i in range(0, N):   #loop through the document
    line = fp.readline()  # reads a single line from the file
    line = line.strip()   # "strip" the line to get the user
    users.append( line)   # add the element to the list without creating a new list
fp.close()

# Open final Time Series Data
fp = file('timeSeries.txt', 'w')
# Initialize the date
t = datetime(2012, 7, 6, 18, 33, 0)  # For syria
#t = datetime(2009, 11, 10, 1, 0, 0)	# For Tiger Woods
dt = timedelta(hours = 6)

# For each time 
for i in range(0, T):
    # For each user
    next = t+dt 
    for j in range(0, N):
        query = "SELECT count(*) FROM hashingtweets WHERE hashvalue = '%s' AND time BETWEEN " % users[j];
        query = query +  "str_to_date('%s %s'" % ( t.date(), t.time()) 
        query = query +  ",'%Y-%m-%d %H:%i:%s') AND "
        query = query +  "str_to_date('%s %s'" % ( next.date(), next.time()) 
        query = query +  ",'%Y-%m-%d %H:%i:%s') AND lower(content) LIKE '%syria%';"
	#print users[j]
        cursor.execute(query)
        row = cursor.fetchone()
        fp.write('%s\t' % row)
    fp.write('\n')
    t = next
    next = next + dt
    print i

cursor.close()
conn.close()
fp.close();
