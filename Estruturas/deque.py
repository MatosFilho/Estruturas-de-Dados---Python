class Deque:

	# Starts the deque as an empty array. Sets the maximum size. The initial queue size is zero
	def __init__(self, maxSize):
		self.__dequeElements = []
		self.__dequeSize = 0
		self.__maxSize = maxSize

	# adds the element in the beginning of the queue
	def push_front(self, elem):
		if not self.isFull():
			self.__dequeElements.insert(0, elem)
			self.__dequeSize += 1
			return True
		return False

	# adds the element in the end of the queue
	def push_back(self, elem):
		if not self.isFull():
			self.__dequeElements.append(elem)
			self.__dequeSize += 1
			return True
		return False

	# removes the element from the beginning of the deque
	def pop_front(self):
		if not self.isEmpty():
			elem = self.__dequeElements[0]
			self.__dequeElements.pop(0)
			self.__dequeSize -= 1
			return elem
		return None

	# removes the element from the end of the deque
	def pop_back(self):
		if not self.isEmpty():
			elem = self.__dequeElements[-1]
			self.__dequeElements.pop(self.__dequeSize-1)
			self.__dequeSize -= 1
			return elem
		return None

	# returns the element at the beginning of the deque
	def front(self):
		if not self.isEmpty():
			return self.__dequeElements[0]
		return None

	# returns the element ay the end of the deque
	def back(self):
		if not self.isEmpty():
			return self.__dequeElements[-1]
		return None

	# returns the deque size
	def length(self):
		return self.__dequeSize

	# check if the queue is empty
	def isEmpty(self):
		if self.__dequeSize == 0:
			return True 
		return False

	# check if the queue is full
	def isFull(self):
		if self.__dequeSize == self.__maxSize:
			return True
		return False

'''
d = Deque(6)
print("Empty: ", d.isEmpty())
print("Full: ", d.isFull())
d.push_back(4)
d.push_front(3)
d.push_back(5)
d.pop_back()
d.pop_front()
print("Deque size: ", d.length())
print("Deque: ", d.dequeElements)
'''