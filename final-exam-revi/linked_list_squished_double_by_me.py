class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def print_list(self):
        if self.root is None:
            return
        cur = self.root
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def double(self):
        if self.root is None:
            return
        cur = self.root
        while cur is not None:
            new_node = Node(cur.data)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

    def squished(self):
        if self.root is None:
            return
        cur = self.root
        while cur.next is not None:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next


def start():
    system = LinkedList()
    system.add_node(2)
    system.add_node(6)
    system.add_node(1)
    system.add_node(1)
    system.add_node(1)
    system.add_node(0)
    system.add_node(9)
    system.add_node(11)
    system.add_node(8)
    system.add_node(8)
    # system.double()
    system.squished()
    system.print_list()


start()

