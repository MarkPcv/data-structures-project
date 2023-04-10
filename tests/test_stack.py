"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


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


class TestStack(unittest.TestCase):
    """Test class for Stack Objects"""

    def test_stack_init(self):
        """
        Tests initialization of Stack class
        """
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_stack_push(self):
        """
        Tests push function of Stack class
        """
        stack = Stack()
        stack.push('I')
        stack.push('am')
        stack.push('here')
        self.assertEqual(stack.top.data, 'here')
        self.assertEqual(stack.top.next_node.data, 'am')
        self.assertEqual(stack.top.next_node.next_node.data, 'I')
        self.assertIsNone(stack.top.next_node.next_node.next_node)

    def test_stack_pop(self):
        """
        Tests pop function of Stack class
        """
        stack_single = Stack()
        stack_single.push('First node')
        data = stack_single.pop()
        self.assertIsNone(stack_single.top)
        self.assertEqual(data, 'First node')

        stack_double = Stack()
        stack_double.push('First node')
        stack_double.push('Second node')
        data = stack_double.pop()
        self.assertEqual(stack_double.top.data, 'First node')
        self.assertEqual(data, 'Second node')

    def test_stack_str(self):
        """
        Tests __str__ dunder methods
        """
        stack = Stack()
        stack.push('First node')
        stack.push('Second node')
        expected_result = 'Second node\nFirst node\n'
        self.assertEqual(str(stack),expected_result)
