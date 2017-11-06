import stack
import pytest

class TestClass:		
	@pytest.fixture
	def my_stack(self):
		return stack.Stack(3)

	def test_empty_stack(self, my_stack):
		assert my_stack.isEmpty() == True
		my_stack.push(4)
		assert my_stack.isEmpty() == False

	def test_full_stack(self, my_stack):
		assert my_stack.isFull() == False
		my_stack.push(1)
		my_stack.push(2)
		my_stack.push(3)
		assert my_stack.isFull() == True

	def test_stack_size(self, my_stack):
		my_stack.push(2)
		my_stack.push(3)
		assert my_stack.length() == 2
		my_stack.push(4)
		assert my_stack.length() == 3
		my_stack.push(5)
		assert my_stack.length() == 3
		my_stack.pop()
		assert my_stack.length() == 2

	def test_stack_top(self, my_stack):
		my_stack.push(3)
		assert my_stack.top() == 3
		my_stack.pop()
		assert my_stack.top() == None

	def test_stack_pull(self, my_stack):
		my_stack.push(3)
		assert my_stack.top() == 3
		my_stack.pull(4)
		assert my_stack.top() == 4
