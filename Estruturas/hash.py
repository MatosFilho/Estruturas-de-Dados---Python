class Cell:

	def __init__(self, key, value):
		self.__key = key
		self.__value = value

	def getKey(self):
		return self.__key

	def getValue(self):
		return self.__value

class Hash:

	def __init__(self, size):
		self.__size = size
		self.__map = [[] for i in range(size)]

	def insertHash(self, key, value):
		newCell = Cell(key, value)
		position = 0
		for p in str(key):
			position += ord(p)
		position = position % self.__size
		self.__map[position].append(newCell)

	def getMap(self):
		return self.__map 


m = str(33)
for i in m:
	print(ord(i))
print(str(33))
map = Hash(7)
map.insertHash(3, 7)
print(map.getMap())