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
		self.__lastNode = None
		self.__listSize = 0

	# adds an element in the linked list
	def insertNode(self, newData, pos):
		if pos >= 0:
			newNode = Node(newData)
			# if empty list
			if self.__listSize == 0:
				self.__firstNode = newNode
				self.__lastNode = newNode
			# if the insertion is in beginning
			elif pos == 0:
				newNode.setNext(self.__firstNode)
				self.__firstNode = newNode
			# if insert position bigger than list size
			elif pos >= self.__listSize:
				self.__lastNode.setNext(newNode)
				self.__lastNode = newNode 
			else:
				currentNode = self.__firstNode
				currentPosition = 0
				while currentPosition != pos - 1:
					currentPosition += 1
					currentNode = currentNode.getNext()
				newNode.setNext(currentNode.getNext())
				currentNode.setNext(newNode)
			self.__listSize += 1
			return True
		else:
			return False

	# removes an element from the list
	def removeNode(self, pos):
		if pos >= 0 and pos < self.__listSize and self.__listSize > 0:
			if self.__listSize == 1:
				self.__firstNode = None
				self.__lastNode = None
			elif pos == 0:
				self.__firstNode = self.__firstNode.getNext()
			else:
				currentPosition = 0
				currentNode = self.__firstNode
				while currentPosition != pos - 1:
					currentPosition += 1
					currentNode = currentNode.getNext()
				currentNode.setNext(currentNode.getNext().getNext())
				if currentPosition == self.__listSize - 2:
					self.__lastNode = currentNode

			self.__listSize -= 1
			return True
		else:
			return False

	# prints list elements 
	def printList(self):
		currentNode = self.__firstNode
		stringList = "["
		while currentNode != None:
			stringList += str(currentNode.getData()) + ", "
			currentNode = currentNode.getNext()
		stringList += "]"
		return stringList

	# returns the number of nodes in the linked list
	def length(self):
		return self.__listSize

'''
l = LinkedList()
l.insertNode("Um nó", 0)
l.insertNode("Dois nó", 0)
l.insertNode("Tres nó", 9)
l.insertNode("Quatro nó", 1)
print("length: ", l.length())
print(l.printList())
'''
