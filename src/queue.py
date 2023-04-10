class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        # Case with no elements
        if self.head is None:
            self.head = Node(data, None)
        # Case with one element
        elif self.tail is None:
            self.tail = Node(data, None)
            self.head.next_node = self.tail
        # Case with at least two elements
        else:
            temp = self.tail
            self.tail = Node(data, None)
            temp.next_node = self.tail


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        # Initialize variables
        result = ""
        temp = self.head
        # From front of queue till the last element
        while temp is not None:
            if temp.next_node is None:
                result += temp.data
            else:
                result += temp.data + '\n'
            temp = temp.next_node

        return result
