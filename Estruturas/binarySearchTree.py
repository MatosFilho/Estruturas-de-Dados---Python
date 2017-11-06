class Node:

	def __init__(self, data):
		self.__data = data
		self.__leftChild = None
		self.__rightChild = None

	def getData(self):
		return self.__data
	
	def setData(seld, newData):
		self.__data = newData

	def getLeftChild(self):
		return self.__leftChild

	def setLeftChild(self, child):
		self.__leftChild = child

	def getRightChild(self):
		return self.__rightChild

	def setRightChild(self, child):
		self.__rightChild = child

class BinarySearchTree:

	def __init__(self):
		self.__root = None

	# inserts a new node in the tree
	def insert(self, value):
		self.insertNode(self.__root, value)

	# runs the tree and insert the node
	def insertNode(self, actualNode, value):
		if self.isEmpty():
			self.__root = Node(value)
		elif value < actualNode.getData():
			if actualNode.getLeftChild() == None:
				actualNode.setLeftChild(Node(value))
			else:
				self.insertNode(actualNode.getLeftChild(), value)
		else:
			if actualNode.getRightChild() == None:
				actualNode.setRightChild(Node(value))
			else:
				self.insertNode(actualNode.getRightChild(), value)

	# removes a node from the tree
	def remove(self, value):
		self.removeNode(None, self.getRoot(), value)

	# runs the tree and remove the node
	def removeNode(self, previousNode, actualNode, value):
		if actualNode != None:
			if actualNode.getData() == value:
				# node is a leaf
				if actualNode.getLeftChild() == None and actualNode.getRightChild() == None:
					# root is the only node in the tree
					if previousNode == None:
						self.__root = None
					elif previousNode.getLeftChild().getData() == value:
						previousNode.setLeftChild(None)
					else:
						previousNode.setRightChild(None)
				# node has only the right child 
				elif actualNode.getLeftChild() == None:
					# node to be removed is the root
					if previousNode == None:
						self.__root = self.__root.getRightChild()
					elif previousNode.getLeftChild().getData() == value:
						previousNode.setLeftChild(actualNode.getRightChild())
					else:
						previousNode.setRightChild(actualNode.getRightChild())
				# node has only the left child
				elif actualNode.getRightChild() == None:
					# node to be removed is the root
					if previousNode == None:
						self.__root = self.__root.getLeftChild()
					elif previousNode.getLeftChild().getData() == value:
						previousNode.setLeftChild(actualNode.getLeftChild())
					else:
						previousNode.setRightChild(actualNode.getLeftChild())
				# node has both childs
				else:
					auxParent = actualNode
					auxChild = actualNode.getRightChild()
					while auxChild.getLeftChild() != None:
						auxParent = auxChild
						auxChild = auxChild.getLeftChild()
					# to make the right conection
					if auxParent.getLeftChild().getData() == auxChild.getData():
						auxParent.setLeftChild(auxChild.getRightChild())
					else:
						auxParent.setRightChild(auxChild.getRightChild())
					# changes the removed node by the smallest element of the right subtree
					auxChild.setLeftChild(actualNode.getLeftChild())
					auxChild.setRightChild(actualNode.getRightChild())
					if previousNode == None:
						self.__root = auxChild
					elif previousNode.getLeftChild().getData() == value:
						previousNode.setLeftChild(auxChild)
					else:
						previousNode.setRightChild(auxChild)
			elif value < actualNode.getData():
				self.removeNode(actualNode, actualNode.getLeftChild(), value)
			else:
				self.removeNode(actualNode, actualNode.getRightChild(), value)
	'''
	# runs and prints the tree in pre-order
	def getTree(self, actualNode):
		tree = ""
		if actualNode != None:
			tree = tree + str(actualNode.getData()) + ", "
			tree += self.getTree(actualNode.getLeftChild())
			tree += self.getTree(actualNode.getRightChild())
		return tree
	'''
	
	# runs the tree in pre-order and returns an array representing the tree
	def getTree(self, actualNode):
		tree = []
		if actualNode != None:
			tree.append(actualNode.getData())
			tree = tree + self.getTree(actualNode.getLeftChild())
			tree = tree + self.getTree(actualNode.getRightChild())
		return tree

	# returns the root of the binary tree
	def getRoot(self):
		return self.__root

	# check if tree is empty
	def isEmpty(self):
		if self.__root == None:
			return True
		return False
		
'''
bst = BinarySearchTree()
print(bst.isEmpty())
print(bst.getRoot())
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)
print(bst.getTree(bst.getRoot()))
'''