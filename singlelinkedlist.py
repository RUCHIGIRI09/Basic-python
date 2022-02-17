class Node:
    def __init__(self, value):
        self.head_node = value
        self.next_node = None
    def value(self):
        return self.head_node
    def next(self):
        return self.next_node
class LinkedList:
    def __init__(self, values=[]):
        self.head_ = None
        self.values = values
        for i in self.values:
            self.push(i)
    def __len__(self):
        current_node = self.head_
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count
    def __iter__(self):
        current = self.head_
        while current is not None:
            yield current.head_node
            current = current.next_node
    def head(self):
        if self.head_ is None:
            raise EmptyListException("The list is empty.")
        return self.head_
    def push(self, value):
        new_node = Node(value)
        if self.head_ is not None:
            new_node.next_node = self.head_
        self.head_ = new_node
    def pop(self):
        if self.head_ is None:
            raise EmptyListException("The list is empty.")
        head_node = self.head_
        self.head_ = head_node.next_node
        node_pop = head_node.head_node
        del head_node
        return node_pop
    def reversed(self):
        current_node = self.head_
        nodes_list = []
        while current_node:
            nodes_list.insert(0, current_node.head_node)
            current_node = current_node.next_node
        return nodes_list
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message