import sys,tweepy,time
import MySQLdb
import pickle
import jsonpickle

#code for jsonpickle
def json_serialize(obj, filename, use_jsonpickle=True):
    f = open(filename, 'w')
    if use_jsonpickle:
        import jsonpickle
        json_obj = jsonpickle.encode(obj)
        f.write(json_obj)
    else:
        simplejson.dump(obj, f) 
    f.close()




#code for the linked list class

class Node: 
  def __init__(self, cargo=None, next=None, ids=None): 
    self.cargo = cargo 
    self.next  = next 
    self.ids =ids
  def tell(self):
  print '(The cargo is %s, the next node is %s, ids is %s)' %(self.cargo,self.next,self.ids)	
  def __str__(self): 
    return str(self.cargo)

class linked_list:
  def __init__(self):
		self.cur_node = None
  def add_node(self, cargo,ids):
			
		new_node = Node() # create a new node
		new_node.ids = ids
		new_node.cargo = cargo
		new_node.next = self.cur_node # link the new node to the 'previous' node.
		self.cur_node = new_node #  set the current node to the new one.

  def list_print(self):
		node = the_list.cur_node
		while node:
			print node.cargo
			print node.ids
			node = node.next	

  def get_node(self,ids):
		node = the_list.cur_node
		print 'JUST start checking '
		#transverse the list to find the right node
		while node.next != None:
			print 'JUST CHECKING for this time'
			
			if node.ids == ids:
			 	print node.ids
			 	print node.cargo
				print node.next
			node = node.next	


#starting the query
database = 'politics2'
table = "obamacare"
#connect to mySQL database
myconnect = MySQLdb.connect(host='localhost',user='root',passwd='qwer1234',db=database)
cursor = myconnect.cursor()


#auth tweepy
CONSUMER_KEY ='Yes924iIs2v8SeUO0mu7WA'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = '86185051-r798E9865tV3THupBF6fj1elNz8sSVfckXqMs23Cx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#first import all the user_ids in the target list
sql = "select distinct user_id from %s "  % table
print "getting user_id from %s" %table
	
n = cursor.execute(sql)
#initialize array to store the distinct user_ids from the databse
target = []



while(1):
	row = cursor.fetchone()	
	if row == None:
		break
	print row
	print type(row)
	print len(row)
	print row[0]
	print type(row[0])
	print len(row[0])
	target.append(row[0])

print target


#search the user with screen_name as row[0] and return the user_id 
#exec 'user_id = api.get_user(screen_name= "%s")' % a
#print user_id

"""while (1):
	row = cursor.fetchone ()
	#print type(row[0])
	len(row)
	if row == None:
		break
	#print row[0]
	u = unicode(row[0], "utf-8")
#	target.append( u)
	
print target		
"""
"""
while (1):
    row = cursor.fetchone ()
	print row[0]
	target.append(row[0])    
	if row == None:
        break

while (1):
    row = cursor.fetchone ()
    if row == None:
        break
	print row[0]
#    target.append(row[0].encode("utf-8"))
"""



cursor.close()
myconnect.close()





#########target = [110358419,90554771]


error = 0


#total =len(target)
#print total
#users= set(target)
#print users
#loop for all target ids

the_list = linked_list()
print "step1"
the_list.list_print()
count=0
for index in range(len(target)):
	exec 'friends_id_%s = []' % target[index]
	print 'friends_id_%s'    %target[index]
	
	try: 
		exec 'friends_id_%s = tweepy.api.friends_ids(target[index])' %target[index]
	except: 
		print 'num of TWEEPY ERROR is :'
		error = error+1
		print error
		continue	
	exec 'the_list.add_node(friends_id_%s,%s)' %(target[index],target[index])

	json_serialize(the_list,table, use_jsonpickle=True)
	count = count+1
	print "this is the %s time" %count
#	exec "output = open('%s.p', 'w')" %table
#	pickle.dump(the_list, output,protocol = pickle.HIGHEST_PROTOCOL)
#	output.close()
	time.sleep(25) 
print "step2"
the_list.list_print()

print "\n\n"
#the_list.get_node(100011309)
print "~~~~STORING IN FILE~~~~"
#exec "output = open('%s.p', 'w')" %table
#output = open('%s.p', 'w')%table
#pickle.dump(the_list, output)
#output.close()





