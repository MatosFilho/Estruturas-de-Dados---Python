# class that represents a node in the linked list
class Node:

	def __init__(self, data):
		self.__data = data
		self.__next = None

	def getData(self):
		return self.__data

	def setData(self, newData):
		self.__data = newData

	def getNext(self):
		return self.__next

	def setNext(self, newNext):
		self.__next = newNext


class LinkedList:

	def __init__(self):
		self.__firstNode = None
		self.__listSize = 0

	# adds an element in the linked list
	def insertNode(self, data):
		if self.__firstNode == None:
			self.__firstNode = Node(data)
		else:
			currentNode = self.__firstNode
			while currentNode.getNext() != None:
				currentNode = currentNode.getNext()
			currentNode.setNext(Node(data))
		self.__listSize += 1

	# removes the first element in the list
	def removeNode(self):
		self.__firstNode = self.__firstNode.getNext()
		self.__listSize -= 1 

	# prints list elements 
	def printList(self):
		currentNode = self.__firstNode
		while currentNode != None:
			print(currentNode.getData(), end = ", ")
			currentNode = currentNode.getNext()
		print()

	# returns the number of nodes in the linked list
	def length(self):
		return self.__listSize

'''
n = Node("dado")
print(n.getData())
print(n.getNext())
l = LinkedList()
l.insertNode("dado")
l.insertNode("mais dado")
print(l.length())
l.printList()
l.removeNode()
print(l.length())
l.printList()
'''