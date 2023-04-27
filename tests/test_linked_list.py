"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList

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

class TestLinkedList(unittest.TestCase):
    """Test class for LinkedList Objects"""
    def test_queue_init(self):
        """
        Tests initialization of LinkedList class
        """
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_insert_beginning(self):
        """
        Tests insertion of element to the start of the list
        """
        linked_list = LinkedList()
        linked_list.insert_beginning({'name': 'Kate'})
        self.assertEqual(linked_list.head, linked_list.tail)
        linked_list.insert_beginning({'name': 'Graig'})
        self.assertEqual(linked_list.head.data, {'name': 'Graig'})
        self.assertEqual(linked_list.tail.data, {'name': 'Kate'})

    def test_insert_at_end(self):
        """
        Tests insertion of element to the start of the list
        """
        linked_list = LinkedList()
        linked_list.insert_at_end({'name': 'Klaus'})
        self.assertEqual(linked_list.head, linked_list.tail)
        linked_list.insert_at_end({'name': 'Freddy'})
        self.assertEqual(linked_list.head.data, {'name': 'Klaus'})
        self.assertEqual(linked_list.tail.data, {'name': 'Freddy'})

    def test_str(self):
        """
        Tests __str__ dunder method
        """
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')
        linked_list.insert_beginning({'name': 'Kate'})
        linked_list.insert_at_end({'name': 'Klaus'})
        linked_list.insert_beginning({'name': 'Graig'})
        linked_list.insert_at_end({'name': 'Freddy'})
        self.assertEqual(str(linked_list), ("{'name': 'Graig'} -> "
                                           "{'name': 'Kate'} -> "
                                           "{'name': 'Klaus'} -> "
                                           "{'name': 'Freddy'} -> None"))

    def test_to_list(self):
        """
        Test conversion from linked list to list
        """
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'mpoc655'})
        ll.insert_at_end({'id': 2, 'username': 'markpcv'})
        ll.insert_at_end({'id': 3, 'username': 'nvrgivep'})
        ll.insert_beginning({'id': 0, 'username': 'blacksmith'})
        self.assertEqual(ll.to_list(), [
                        {'id': 0, 'username': 'blacksmith'},
                        {'id': 1, 'username': 'mpoc655'},
                        {'id': 2, 'username': 'markpcv'},
                        {'id': 3, 'username': 'nvrgivep'},
        ])

    def test_get_data_by_id(self):
        """
        Test search by id
        """
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'mpoc655'})
        ll.insert_at_end('herewego')
        ll.insert_at_end([4, 5, 6])
        ll.insert_at_end({'id': 2, 'username': 'spider345'})

        self.assertRaises(TypeError, ll.get_data_by_id(2))

        self.assertEqual(ll.get_data_by_id(2),
                         {'id': 2, 'username': 'spider345'})