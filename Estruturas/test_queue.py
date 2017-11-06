import pytest
import queue

class TestQueue:

	@pytest.fixture
	def my_queue(self):
		return queue.Queue(5)

	def test_queue_empty(self, my_queue):
		assert my_queue.isEmpty() == True
		assert my_queue.dequeue() == None
		my_queue.enqueue(5)
		assert my_queue.isEmpty() == False

	def test_queue_full(self, my_queue):
		assert my_queue.isFull() == False
		my_queue.enqueue(1)
		my_queue.enqueue(2)
		my_queue.enqueue(3)
		my_queue.enqueue(4)
		my_queue.enqueue(5)
		assert my_queue.isFull() == True
		assert my_queue.enqueue(7) == None

	def test_queue_length(self, my_queue):
		assert my_queue.length() == 0
		my_queue.enqueue(4)
		my_queue.enqueue(4)
		my_queue.enqueue(4)
		assert my_queue.length() == 3
		my_queue.dequeue()
		assert my_queue.length() == 2

	def test_queue_front(self, my_queue):
		assert my_queue.front() == None
		my_queue.enqueue(5)
		assert my_queue.front() == 5
		my_queue.enqueue(9)
		my_queue.enqueue(17)
		assert my_queue.front() == 5
		my_queue.dequeue()
		assert my_queue.front() == 9


