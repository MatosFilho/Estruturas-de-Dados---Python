class Stack:

	# Starts the stack as an empty array. Sets the maximum size. The initial stack size is zero
	def __init__(self, maxSize):
		self.stackElements = []
		self.stackSize = 0
		self.maxSize = maxSize

	# adds element in the top of the stack
	def push(self, elem):
		if not self.isFull():
			self.stackElements.append(elem)
			self.stackSize += 1
		return None

	# removes the element from the top of the stack and returns it
	def pop(self):
		if not self.isEmpty():
			elem = self.stackElements[self.stackSize-1]
			self.stackElements.pop(self.stackSize-1)
			self.stackSize -= 1
			return elem
		return None

	# replaces the top of the stack
	def pull(self, elem):
		if not self.isEmpty():
			self.stackElements.pop(self.stackSize-1)
			self.stackElements.append(elem)
		return None

	# returns the element in the top of the stack
	def top(self):
		if not self.isEmpty():
			return self.stackElements[self.stackSize-1]
		return None

	# returns the stack size
	def length(self):
		return self.stackSize

	# checks if the stack is empty
	def isEmpty(self):
		if self.stackSize == 0:
			return True
		return False

	# checks if the stack is full
	def isFull(self):
		if self.stackSize == self.maxSize:
			return True
		return False

