class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.data = (name, score)
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.tail = None

    def add_node(self, name, score):
        new_node = Node(name, score)
        if self.root is None:
            self.root = new_node
            self.tail = new_node
            self.root.next = None
            self.tail.prev = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

    def size(self):
        count = 0
        cur = self.root
        if self.root is None:
            return 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def print_list(self):
        if self.root is None:
            return
        cur = self.root
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def order(self):
        if self.root is None:
            return
        prev = self.root
        while prev.next is not None:
            cur = prev.next
            while cur is not None:
                if prev.score > cur.score:
                    val = cur.data
                    val_name = cur.name
                    val_score = cur.score
                    cur.data = prev.data
                    cur.name = prev.name
                    cur.score = prev.score
                    prev.name = val_name
                    prev.score = val_score
                    prev.data = val
                cur = cur.next
            prev = prev.next

    def retrieve_score(self, in_score):
        if self.root is None:
            return
        cur = self.root
        for i in range(self.size()):
            if cur.score == in_score:
                print(cur.data)
            cur = cur.next

    def delete(self, in_name):
        if self.root is None:
            return
        prev = self.root
        cur = prev.next
        while cur.name != in_name:
            cur = cur.next
        if cur == self.tail:
            cur = None
            cur.data = None
        else:
            cur.data = cur.next.data
            cur.name = cur.next.name
            cur.score = cur.next.score
            cur.next = cur.next.next

    def update(self, in_name, in_score):
        if self.root is None:
            return
        cur = self.root
        while cur.name != in_name:
            cur = cur.next
        cur.score = in_score
        cur.data = (cur.name, in_score)


def start():
    system = LinkedList()
    system.add_node("Mill", 2)
    system.add_node("Ton", 5)
    system.add_node("Mile", 1)
    system.add_node("Foam", 9)
    system.add_node("Cypher", 2)
    # system.print_list()
    # system.retrieve_score(2)
    system.delete("Ton")
    system.update("Mill", 10)
    system.print_list()


start()
