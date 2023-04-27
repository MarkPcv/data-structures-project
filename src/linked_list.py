class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел
        с этими данными в начало связанного списка"""
        # Case with no elements
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        # Case with at least one element
        else:
            temp = self.head
            self.head = Node(data, temp)


    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел
        с этими данными в конец связанного списка"""
        # Case with no elements
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        # Case with at least one element
        else:
            temp = self.tail
            self.tail = Node(data, None)
            temp.next_node = self.tail

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = f'{str(node.data)} ->'
        node = node.next_node
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self) -> list:
        """
        Converts linked list into a list
        """
        list_elements = []
        temp = self.head
        while temp is not None:
            list_elements.append(temp.data)
            temp = temp.next_node
        return list_elements

    def get_data_by_id(self, element_id: int) -> dict:
        """
        Returns a dictionary by id
        """
        temp = self.head
        while temp is not None:
            try:
                if temp.data['id'] == element_id:
                    return temp.data
                temp = temp.next_node
            except TypeError:
                print(TypeError("Data is not a dictionary or there is no 'id'"))
                temp = temp.next_node
