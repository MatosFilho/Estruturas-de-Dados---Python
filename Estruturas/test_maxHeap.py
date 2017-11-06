import maxHeap
import pytest

class TestMaxHeap:

	@pytest.fixture
	def heap(self):
		return maxHeap.MaxHeap()

	def test_one_insertion(self, heap):
		heap.insert("vermelho", 25)
		assert heap.show() == [25]

	def test_two_insertions(self, heap):
		heap.insert("vermelho", 25)
		heap.insert("verde", 30)
		assert heap.show() == [30, 25]
	
	def test_multiple_insertions(self, heap):
		heap.insert("vermelho", 25)
		heap.insert("verde", 30)
		assert heap.show() == [30, 25]
		heap.insert("amarelo", 15)
		heap.insert("vermelho-escuro", 25)
		assert heap.show() == [30, 25, 15, 25]
		heap.insert("azul", 60)
		assert heap.show() == [60, 30, 15, 25, 25]

	def test_remove_empty_heap(self, heap):
		assert heap.remove() == False

	def test_remove_unary_heap(self, heap):
		heap.insert("preto", 5)
		heap.remove()
		assert heap.show() == []

	def test_remove_heap_multiple_elements(self, heap):
		heap.insert("azul", 60)
		heap.insert("vermelho", 25)
		heap.insert("verde", 30)
		heap.insert("amarelo", 15)
		heap.insert("vermelho-escuro", 25)
		assert heap.show() == [60, 25, 30, 15, 25]
		heap.remove()
		assert heap.show() == [30, 25, 25, 15]

	def test_remove_especial_case(self, heap):
		heap.insert("azul", 60)
		heap.insert("verde", 30)
		heap.insert("vermelho", 25)
		heap.insert("amarelo", 15)
		heap.insert("vermelho-escuro", 5)
		assert heap.show() == [60, 30, 25, 15, 5]
		heap.remove()
		assert heap.show() == [30, 15, 25, 5]

		
