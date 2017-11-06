import deque
import pytest

class TestDeque:

	@pytest.fixture
	def my_deque(self):
		return deque.Deque(6)

	def test_deque_empty(self, my_deque):
		assert my_deque.isEmpty() == True
		assert my_deque.pop_back() == None
		assert my_deque.pop_front() == None
		my_deque.push_front(4)
		assert my_deque.isEmpty() == False

	def test_deque_full(self, my_deque):
		assert my_deque.isFull() == False
		my_deque.push_front(1)
		my_deque.push_front(2)
		my_deque.push_front(3)
		my_deque.push_front(4)
		my_deque.push_front(5)
		my_deque.push_front(6)
		assert my_deque.isFull() == True
		assert my_deque.push_front(7) == False
		assert my_deque.push_back(8) == False

	def test_deque_length(self, my_deque):
		assert my_deque.length() == 0
		my_deque.push_front(7)
		my_deque.push_back(9)
		assert my_deque.length() == 2
		
	def test_deque_front_back(self, my_deque):
		assert my_deque.front() == None
		assert my_deque.back() == None
		my_deque.push_front(8)
		assert my_deque.front() == 8
		assert my_deque.back() == 8
		my_deque.push_front(7)
		my_deque.push_back(18)
		assert my_deque.front() == 7
		assert my_deque.back() == 18