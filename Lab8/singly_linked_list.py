class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data
        return new_data

    def set_next(self, new_next):
        self.next = new_next
        return new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, element):
        num = Node(element)
        num.set_next(self.head)
        self.head = num

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
            try:
                print(previous.get_data())
                previous = previous.get_next()
            except AttributeError:
                exit()
        exit()

    def squish(self, length):
        squished_list = []
        current = self.head
        previous = current
        current = current.get_next()
        for i in range(length):
            if current is None:
                if squished_list[-1] != previous.get_data():
                    squished_list.append(previous.get_data())
                break
            if len(squished_list) > 0:
                if previous.get_data() == current.get_data() and squished_list[-1] != previous.get_data():
                    squished_list.append(previous.get_data())
                    previous = current
                    current = current.get_next()
                elif previous.get_data() != current.get_data() and squished_list[-1] != previous.get_data():
                    squished_list.append(previous.get_data())
                    previous = current
                    current = current.get_next()
                else:
                    previous = current
                    current = current.get_next()
            else:
                squished_list.append(previous.get_data())
                previous = current
                current = current.get_next()
        return squished_list

    def double(self, my_list):
        previous = self.head
        while previous is not None:
            new_node = Node(previous.get_data())
            try:
                new_node.set_next(previous.get_next())
            except:
                new_node.set_next(None)
                break
            previous.set_next(new_node)
            previous = new_node.get_next()
        my_list.print()


def start():
    my_list = UnorderedList()
    length = int(input("Insert length of list : "))
    print("Enter number : ")
    for i in range(length):
        my_list.add(int(input()))
    print(my_list.squish(length))
    print(my_list.double(my_list))


start()
