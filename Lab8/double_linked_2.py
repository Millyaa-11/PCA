class Node:
    def __init__(self, data):
        self.data = data
        self.name = data[0]
        self.score = data[1]
        self.previous = None
        self.next = None

    def get_name(self):
        return self.name


class SortList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if self.head is None:
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.previous = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None

    def sortList(self):
        # Check whether list is empty
        if self.head is None:
            return
        else:
            # Current will point to head
            current = self.head
            while current.next is not None:
                # Index will point to node next to current
                index = current.next
                while index is not None:
                    # If current's data is greater than index's data, swap the data of current and index
                    if current.score > index.score:
                        temp = current.data
                        temp_name = current.name
                        temp_score = current.score
                        current.data = index.data
                        current.name = index.name
                        current.score = index.score
                        index.data = temp
                        index.name = temp_name
                        index.score = temp_score
                    index = index.next
                current = current.next
        return

    def display(self):
        # Node current will point to head
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while current is not None:
            # Prints each node by incrementing pointer.
            print(current.data)
            current = current.next

    def deleteNode(self, element):
        node = self.head
        while node.name != element:
            node = node.next
        if node == self.tail:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next
        return

    def update(self):
        current = self.head



players_list = SortList()
length = int(input("Enter number of players : "))
for i in range(length):
    name = input("Input player's name : ")
    score = int(input("Input player's score : "))
    player = Node((name, score))
    players_list.addNode((name, score))
# Sorting list
players_list.sortList()
players_list.display()


print("Enter A to add new player's name and score\n"
      "Enter D to delete player's information\n"
      "Enter P to print scores\n"
      "Enter U to update the score\n"
      "Enter Q to exit\n")
ans = input()
if ans == "A":
    name = input("Input player's name : ")
    score = int(input("Input player's score : "))
    players_list.addNode((name, score))
    players_list.sortList()
    players_list.display()
if ans == "D":
    del_name = input("Input player's name : ")
    players_list.deleteNode(del_name)
    players_list.display()
if ans == "P":
    players_list.sortList()
    players_list.display()
if ans == "U":
    update_name = input("Input player's name to update score : ")



