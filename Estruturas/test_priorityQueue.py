import priorityQueue
import pytest

class TestPriorityQueue:

	@pytest.fixture
	def pqueue(self):
		return priorityQueue.PriorityQueue()

	def test_empty(self, pqueue):
		assert pqueue.isEmpty() == True
		assert pqueue.length() == 0

	def test_insert_elements(self, pqueue):
		pqueue.insert("bola", 10)
		pqueue.insert("livro", 20)
		assert pqueue.length() == 2

	def test_show_pqueue(self, pqueue):
		pqueue.insert("bola", 10)
		pqueue.insert("livro", 20)
		assert pqueue.show() == [('livro', 20), ('bola', 10)]

	def test_remove_element(self, pqueue):
		pqueue.insert("bola", 10)
		pqueue.insert("livro", 20)
		pqueue.insert("cerveja", 30)
		assert pqueue.show() == [('cerveja', 30), ('livro', 20), ('bola', 10)]
		assert pqueue.remove().getPriority() == 30
		assert pqueue.show() == [('livro', 20), ('bola', 10)]