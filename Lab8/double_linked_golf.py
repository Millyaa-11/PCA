class Node:
    def __init__(self, name, score):
        self.data = (name, score)
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

    def get_data(self):
        return self.name, self.score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_next(self):
        return self.next

    def set_data(self, new_name, new_score):
        self.name = new_name
        self.score = new_score

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

    def get_prev(self):
        return self.prev


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, name, score):
        newNode = Node(name, score)
        if self.head is None:
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.prev = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.prev = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print(self):
        previous = self.head
        while previous is not None:
            if previous.get_next() is None:
                print(previous.get_data())
                break
            try:
                print(previous.get_data())
                previous = previous.get_next()
            except AttributeError:
                exit(1)

    def sort_score(self):
        # Check whether list is empty
        if self.head is None:
            return
        else:
            current = self.head
            while current.next is not None:
                cur_next = current.next
                while cur_next is not None:
                    # If current's data is greater than index's data, swap the data of current and next_cur
                    if current.score > cur_next.score:
                        temp = current.data
                        print(current.score, "current1")
                        current.data = cur_next.data
                        cur_next.data = temp
                    cur_next = cur_next.next
                    try:
                        print(current.score,"current")
                        print(current.next.score)
                        print(cur_next.score, "cur_next")
                    except:
                        continue
                current = current.next


def start():
    players_list = UnorderedList()
    length = int(input("Enter number of players : "))
    for i in range(length):
        name = input("Input player's name : ")
        score = int(input("Input player's score : "))
        player = Node(name, score)
        players_list.add(player.name, player.score)
    players_list.print()
    print("\n \nAfter")
    players_list.sort_score()
    players_list.print()


start()
