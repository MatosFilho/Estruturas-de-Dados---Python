class Node:

	def __init__(self, identifier, value):
		self.__id = identifier
		self.__priority = value

	def getId(self):
		return self.__id

	def getPriority(self):
		return self.__priority

class PriorityQueue:

	# creates an priority queue like an empty array. Initial size is zero
	def __init__(self):
		self.__pQueue = []
		self.__size = 0

	# inserts a node in the priority queue
	def insert(self, identifier, priority):
		newNode = Node(identifier, priority)
		if self.isEmpty():
			self.__pQueue = [newNode]
		else:
			inserted = False
			for i in range(self.__size):
				if priority > self.__pQueue[i].getPriority():
					self.__pQueue.insert(i, newNode)
					inserted = True
					break
			if not inserted:
				self.__pQueue.append(newNode)
		self.__size += 1

	# removes the first node and returns it
	def remove(self):
		if self.isEmpty():
			return False
		elem = self.__pQueue.pop(0)
		return elem


	# returns a representation of the priority queue
	def show(self):
		auxQueue = []
		for node in self.__pQueue:
			auxQueue.append((node.getId(), node.getPriority()))
		return auxQueue

	# returns priority queue size
	def length(self):
		return self.__size

	# checks if the priority queue is empty
	def isEmpty(self):
		if self.__size == 0:
			return True
		return False

pqueue = PriorityQueue()
pqueue.insert("bola", 10)
pqueue.insert("livro", 20)
print(pqueue.show())