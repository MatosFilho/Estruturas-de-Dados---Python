import linkedList
import pytest

class TestLinkedList:

	@pytest.fixture
	def my_list(self):
		return linkedList.LinkedList()

	def test_list_length(self, my_list):
		assert my_list.length() == 0
		assert my_list.insertNode("dado", -2) == False
		assert my_list.length() == 0
		assert my_list.insertNode("dado", 0) == True
		assert my_list.length() == 1

	def test_list_insertion(self, my_list):
		assert my_list.length() == 0
		my_list.insertNode("um", 7)
		assert my_list.printList() == "[um, ]"
		my_list.insertNode("dois", 0)
		assert my_list.printList() == "[dois, um, ]"
		my_list.insertNode("três", 4)
		assert my_list.printList() == "[dois, um, três, ]"
		my_list.insertNode(4, 1)
		assert my_list.printList() == "[dois, 4, um, três, ]"
		my_list.insertNode(5, 3)
		assert my_list.printList() == "[dois, 4, um, 5, três, ]"

	def test_list_removal(self, my_list):
		assert my_list.removeNode(2) == False
		my_list.insertNode(1, 0)
		my_list.insertNode(2, 1)
		my_list.insertNode(3, 2)
		my_list.insertNode(4, 3)
		my_list.insertNode(5, 4)
		my_list.insertNode(6, 5)
		assert my_list.length() == 6
		assert my_list.printList() == "[1, 2, 3, 4, 5, 6, ]"
		assert my_list.removeNode(-3) == False
		assert my_list,removeNode(10) == False
		assert my_list.printList() == "[1, 2, 3, 4, 5, 6, ]"
		my_list.removeNode(0)
		assert my_list.length() == 5
		assert my_list.printList() == "[2, 3, 4, 5, 6, ]"
		my_list.removeNode(2)
		assert my_list.length() == 4
		assert my_list.printList() == "[2, 3, 5, 6, ]"
		my_list.removeNode(3)
		my_list.insertNode(7, 10)
		assert my_list.printList() == "[2, 3, 5, 7, ]"

