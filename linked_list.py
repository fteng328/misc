#! /usr/bin/env python

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
		node = ll.cur_node
		while node:
			print node.cargo
			print node.ids
			node = node.next	

  def get_node(self,ids):
		node = ll.cur_node
		print 'J1111UST CHECKING'
		#transverse the list to find the right node
		while node.next != None:
			print 'JUST CHECKING for this time'
			
			if node.ids == ids:
			 	print node.ids
			 	print node.cargo
				print node.next
			node = node.next	

		
list1= [1,23,4,5,]
list2= [3,1,4,6,4,32]
list3=[123,432,453,5,53]
list4=[34,3,4,5,6,7,2]
list5=[23,4,5,6,2]

ll = linked_list()
ll.add_node(0,0)
ll.add_node(list1,123456789)
ll.add_node(list2,12345)
ll.add_node(list3,3)
ll.add_node(list4,4)
ll.add_node(list5,6)
ll.add_node(list1,6)
ll.list_print()


#ll.get_node(123456789)
#ll.get_node(3)
ll.get_node(6)

print 'NEW START\n'
def is_follow(id1,id2):
	B= id1
	exec "C= set(list%s)" %id2
	print (B in C)	
	return   (B in C)


is_follow (35,4)


'''
ll.get_node(3)

#help(Node)
node = Node (cargo="test",ids = '12345')
node.tell()
print node

node1 = Node(1,123) 
node2 = Node(2) 
node3 = Node(3) 

node1.tell()
node2.tell()
node3.tell()
'''
'''print node


node1.next = node2
node2.next = node3 


def printList(node): 
  while node: 
    print node, 
    node = node.next 
  print 

def printBackward(list): 
  if list == None: return 
  head = list 
  tail = list.next 
  printBackward(tail) 
  print head, 


printList(node1)
printList(node2)
printList(node3)
'''
"""
class linked_list:
	def __init__(self):
		self.cur_node = None

	def add_node(self, data):
		new_node = node() # create a new node
		new_node.data = data
		new_node.next = self.cur_node # link the new node to the 'previous' node.
		self.cur_node = new_node #  set the current node to the new one.

	def list_print(self):
		node = ll.cur_node
		while node:
			print node.data
			node = node.next	

	def get_node(self,data):
		des_node = node()
		des_node = self.cur_node() #create new node
		print des_node.data

	

	
		
list1= [1,23,4,5,]
list2= [3,1,4,6,4,32]
ll = linked_list()
ll.add_node(list1)
ll.add_node(list2)
ll.add_node(3)
ll.list_print()

ll.get_node(3)

"""
