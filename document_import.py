#This is the python code for importing tweets to mySQL

import  MySQLdb, tweepy, sys, time 

database = 'twitter'
init =0

#how many seconds between each interval
stoptime = 5   

#how many times this script will run
end =30   

#counter for the rows in the database
num_rows_COUNTER= 'a'

#setting up keyword we want to search for
KEYWORD = 'olympics'

#Aside:the product of (stoptime*end) will be the duration at which we run this for
try:
  #we can specify the time of running
	#while(0<time.asctime() < 'Mon Jul  2 10:42:03 2012'):
	while(1):
		print 'hello'
		time.sleep(stoptime)

		#authentication of tweepy API
		CONSUMER_KEY ='Yes924iIs2v8SeUO0mu7WA'
		CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		ACCESS_KEY = '86185051-r798E9865tV3THupBF6fj1elNz8sSVfckXqMs23Cx'
		ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		api = tweepy.API(auth)
		 
		#connect to mySQL database
		myconnect = MySQLdb.connect(host='localhost',user='root',passwd='qwer1234',db=database)

		cursor = myconnect.cursor()
		 
		#starting to execute SQL select statement
		count =0  #total num. of tweets fetched

		#search for tweets which consists of the Keyword we specify
		public1tweet = api.search(q=KEYWORD,rpp=100)  #fetch 95 tweets at a time (Max is around 100)

		#iterate through each tweet, Parsing their Metadata into mySQL database
		for twwt in public1tweet:

			#encode the content and user_name string in order to avoid UnicodeError
			a = twwt.text.encode("utf-8")
			b = twwt.from_user_name.encode("utf-8")

			# import into database/ 'ignore' eliminate duplicates / 'hashingtweets' is destination table
			sql = "insert ignore into hashingtweets(time,content,by_user) values(%s,%s, %s)"		
			param = (twwt.created_at, a, b)		
			count = count +1	
		
			try:	
				n = cursor.execute(sql,param)					
			except: print ' ~~~~~~~~~THERE IS AN ERROR~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	
		print 'How many tweets sampled:' + str(count)
		print 'DONE importing!'

		#~~~check if the database has new data input~~~#
		#getting the number of current rows in the database
		sqlcount = ' select count(*) from hashingtweets'	
		cursor.execute(sqlcount)	
		num_rows_current =  cursor.fetchone() #inorder to get this parameter we have to fetch the number in the query table

		rows = '%s' % num_rows_current
	
		if (num_rows_COUNTER == num_rows_current):
			print 'DID NOT ADD ANY ROWS INTO OUR DATABASE~~'
			print 'num_rows_COUNTER = %s , num_rows_current= %s' % (num_rows_COUNTER, num_rows_current)
		else :
			print 'number of rows currently in database: %s' %(num_rows_current)
			print 'number of rows in counter: %s' %(num_rows_COUNTER)
			num_rows_COUNTER = rows
		print 'DONE CHECKING!'
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		print 'Number of Iterations:'	+ str(init)

		if(init==end ):   #testing this for 1 min
			break
		init=init+1
except KeyboardInterrupt:
	print'\ndetected KEYBOARD INTERUPT'
finally:
	#close
	cursor.close()  	 
	myconnect.close()  
	print 'close connection to database'
	 
print 'PROJECT DONE!!!'
