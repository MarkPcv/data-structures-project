"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue

class TestNode(unittest.TestCase):
    """Test class for Node Objects"""

    def test_node_init(self):
        """
        Tests initialization of Node class
        """
        node1 = Node('New York', None)
        node2 = Node(555, node1)
        self.assertEqual(node1.data, 'New York')
        self.assertEqual(node2.data, 555)
        self.assertTrue(isinstance(node1,Node))
        self.assertIs(node1, node2.next_node)

class TestQueue(unittest.TestCase):
    """Test class for Queue Objects"""

    def test_queue_init(self):
        """
        Tests initialization of Queue class
        """
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_queue_str(self):
        """
        Tests __str__ dunder methods
        """
        queue = Queue()
        queue.enqueue('First node')
        queue.enqueue('Second node')
        queue.enqueue('Third node')
        expected_result = 'First node\nSecond node\nThird node'
        self.assertEqual(str(queue),expected_result)

    def test_queue_enqueue(self):
        """
        Tests enqueue method of Queue class
        """
        queue = Queue()
        queue.enqueue('head')
        queue.enqueue('middle1')
        queue.enqueue('middle2')
        queue.enqueue('middle3')
        queue.enqueue('tail')
        self.assertEqual(queue.head.data, 'head')
        self.assertEqual(queue.head.next_node.data, 'middle1')
        self.assertEqual(queue.head.next_node.next_node.data, 'middle2')
        self.assertEqual(queue.head.next_node.next_node.next_node.data, 'middle3')
        self.assertEqual(queue.tail.data, 'tail')

    def test_queue_dequeue(self):
        """
        Tests enqueue method of Queue class
        """
        queue = Queue()
        queue.enqueue('head')
        queue.enqueue('middle1')
        queue.enqueue('middle2')
        queue.enqueue('middle3')
        queue.enqueue('tail')
        self.assertEqual(queue.dequeue(), 'head')
        self.assertEqual(queue.dequeue(), 'middle1')
        self.assertEqual(queue.dequeue(), 'middle2')
        self.assertEqual(queue.dequeue(), 'middle3')
        self.assertEqual(queue.dequeue(), 'tail')
        self.assertIsNone(queue.dequeue())
