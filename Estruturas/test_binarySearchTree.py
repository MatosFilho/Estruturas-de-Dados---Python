import binarySearchTree
import pytest

class TestBinarySearchTree:

	@pytest.fixture
	def bst(self):
		return binarySearchTree.BinarySearchTree()

	def test_empty_tree(self, bst):
		assert bst.isEmpty() == True

	def test_get_root(self, bst):
		assert bst.getRoot() == None
		bst.insert(8)
		assert bst.isEmpty() == False
		assert bst.getRoot().getData() == 8
		bst.insert(7)
		assert bst.getRoot().getData() == 8

	def test_get_tree(self, bst):
		bst.insert(8)
		bst.insert(3)
		bst.insert(9)
		bst.insert(4)
		assert bst.getTree(bst.getRoot()) == [8, 3, 4, 9]

	def test_remove_leaf(self, bst):
		bst.insert(5)
		assert bst.getTree(bst.getRoot()) == [5]
		bst.insert(2)
		bst.insert(18)
		bst.insert(3)
		bst.insert(-4)
		assert bst.getTree(bst.getRoot()) == [5, 2, -4, 3, 18]
		bst.remove(-4)
		assert bst.getTree(bst.getRoot()) == [5, 2, 3, 18]

	def test_remove_node_with_one_child(self, bst):
		bst.insert(5)
		bst.insert(2)
		bst.insert(18)
		bst.insert(3)
		bst.insert(21)
		bst.insert(19)
		bst.insert(25)
		assert bst.getTree(bst.getRoot()) == [5, 2, 3, 18, 21, 19, 25]
		bst.remove(18)
		assert bst.getTree(bst.getRoot()) == [5, 2, 3, 21, 19, 25]
		bst.remove(2)
		assert bst.getTree(bst.getRoot()) == [5, 3, 21, 19, 25]

	def test_remove_node_with_two_childs(self, bst):
		bst.insert(5)
		bst.insert(2)
		bst.insert(-4)
		bst.insert(12)
		bst.insert(3)
		bst.insert(9)
		bst.insert(21)
		bst.insert(19)
		bst.insert(25)
		assert bst.getTree(bst.getRoot()) == [5, 2, -4, 3, 12, 9, 21, 19, 25]
		bst.remove(12)
		assert bst.getTree(bst.getRoot()) == [5, 2, -4, 3, 19, 9, 21, 25]

	def test_remove_element_dont_exist(self, bst):
		bst.insert(5)
		bst.insert(8)
		assert bst.getTree(bst.getRoot()) == [5, 8]
		bst.remove(9)
		assert bst.getTree(bst.getRoot()) == [5, 8]

	def test_remove_tree_with_only_root(self, bst):
		bst.insert(7)
		assert bst.getTree(bst.getRoot()) == [7]
		bst.remove(7)
		assert bst.isEmpty() == True

	def test_remove_root_with_one_child(self, bst):
		bst.insert(8)
		bst.insert(5)
		bst.insert(3)
		bst.insert(6)
		assert bst.getTree(bst.getRoot()) == [8, 5, 3, 6]
		bst.remove(8)
		assert bst.getTree(bst.getRoot()) == [5, 3, 6]

	def test_remove_root_with_two_childs(self, bst):
		bst.insert(8)
		bst.insert(3)
		bst.insert(1)
		bst.insert(6)
		bst.insert(4)
		bst.insert(7)
		bst.insert(10)
		bst.insert(14)
		bst.insert(13)
		assert  bst.getTree(bst.getRoot()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]
		bst.remove(8)
		assert bst.getTree(bst.getRoot()) == [10, 3, 1, 6, 4, 7, 14, 13]

	def test_remove_udemy_error(self, bst):
		bst.insert(8)
		bst.insert(3)
		bst.insert(1)
		bst.insert(6)
		bst.insert(4)
		bst.insert(5)
		bst.insert(7)
		bst.insert(10)
		bst.insert(14)
		bst.insert(13)
		assert bst.getTree(bst.getRoot()) == [8, 3, 1, 6, 4, 5, 7, 10, 14, 13]
		bst.remove(3)
		assert bst.getTree(bst.getRoot()) == [8, 4, 1, 6, 5, 7, 10, 14, 13]
