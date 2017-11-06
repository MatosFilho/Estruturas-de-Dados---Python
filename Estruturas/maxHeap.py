class Node:

	def __init__(self, identifier, priority):
		self.__id = identifier
		self.__priority = priority

	def getId(self):
		return self.__id

	def getPriority(self):
		return self.__priority

class MaxHeap:

	def __init__(self):
		self.__heap = []
		self.__heapSize = 0

	# inserts element at the end of the heap and then sorts
	def insert(self, identifier, priority):
		newNode = Node(identifier, priority)
		self.__heap.append(newNode)
		# retrieves the position of the inserted node
		position = self.__heapSize
		while position > 0:
			# takes the position of the node father
			if position % 2 == 1:
				parent = (position - 1)//2
			else:
				parent = (position - 2)//2
			if self.__heap[parent].getPriority() < self.__heap[position].getPriority():
				self.__heap[parent], self.__heap[position] = self.__heap[position], self.__heap[parent]
				position = parent
			else:
				break
		self.__heapSize += 1

	# removes the first element from the heap and then reorders it
	def remove(self):
		if not self.isEmpty():
			# remove the first element
			elem = self.__heap.pop(0)
			# decrements heap size
			self.__heapSize -= 1
			if not self.isEmpty():
				# remove the last element
				last = self.__heap.pop(self.__heapSize - 1)
				# puts the last element on the top
				self.__heap.insert(0, last)
				# reorders the heap
				position = 0
				while 2*position + 1 < self.__heapSize:
					left = 2 * position + 1
					right = 2 * position + 2
					# verifies if exist right child
					if right < self.__heapSize:
						# verifies which child is bigger
						if self.__heap[left].getPriority() >= self.__heap[right].getPriority():
							# verifies if parent is smaller than left child
							if self.__heap[position].getPriority() < self.__heap[left].getPriority():
								self.__heap[position], self.__heap[left] = self.__heap[left], self.__heap[position]
								position = left
							else:
								break
						else:
							# verifies if parent is smaller than right child
							if self.__heap[position].getPriority() < self.__heap[right].getPriority():
								self.__heap[position], self.__heap[right] = self.__heap[right], self.__heap[position]
								position = right
							else:
								break
					# if only exists the left child
					else:
						if self.__heap[position].getPriority() < self.__heap[left].getPriority():
								self.__heap[position], self.__heap[left] = self.__heap[left], self.__heap[position]
								break
				return elem
		return False

	# returns heap sizes
	def length(self):
		return self.__heapSize

	# returns an array representing the heap
	def show(self):
		heap = []
		for elem in self.__heap:
			heap.append(elem.getPriority())
		return heap

	# checks if heap is empty
	def isEmpty(self):
		if self.__heapSize == 0:
			return True
		return False

'''
heap = MaxHeap()
heap.insert("key", 40)
print(heap.show())
'''