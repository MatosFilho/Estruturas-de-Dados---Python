class Queue:

	# Starts the queue as an empty array. Sets the maximum size. The initial queue size is zero
	def __init__(self, maxSize):
		self.__queueElements = []
		self.__queueSize = 0
		self.__maxSize = maxSize

	# adds an element in the final of the queue
	def enqueue(self, elem):
		if not self.isFull():
			self.__queueElements.append(elem)
			self.__queueSize += 1
		else:
			return None

	# removes the element from the inicial of the queue and returns it 
	def dequeue(self):
		if not self.isEmpty():
			elem = self.__queueElements[0]
			self.__queueElements.pop(0)
			self.__queueSize -= 1
			return elem
		return None

	# returns the element in the inicial of the queue
	def front(self):
		if not self.isEmpty():
			return self.__queueElements[0]
		return None

	# returns the queue size
	def length(self):
		return self.__queueSize

	# checks if the queue is empty
	def isEmpty(self):
		if self.__queueSize == 0:
			return True
		return False

	# check if the queue is full
	def isFull(self):
		if self.__queueSize == self.__maxSize:
			return True
		return False

'''
q = Queue(5)
print("Empty: ",q.isEmpty())
print("Full: ", q.isFull())
q.enqueue(3)
q.enqueue(7)
print("Size: ", q.length())
print(q.queueSize)
'''