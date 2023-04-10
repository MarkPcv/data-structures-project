class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """
        Returns a string representation of class instance
        """
        # Initialize variables
        result = ""
        temp = self.top
        # From end of stack till the first element
        while temp is not None:
            result += temp.data + '\n'
            temp = temp.next_node

        return result

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top is None:
            self.top = Node(data, None)
        else:
            temp = self.top
            self.top = Node(data, temp)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        # Retrieve data from last element of stack
        data = self.top.data
        # Change top reference to next element
        self.top = self.top.next_node
        return data
