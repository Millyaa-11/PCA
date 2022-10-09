class Node:
    def __init__(self, data):
        self.data = (name, score)
        self.score = score
        self.previous = None
        self.next = None


class SortList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addNode() will add a node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if (self.head == None):
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

            # sortList() will sort the given list in ascending order

    def sortList(self):
        # Check whether list is empty
        if (self.head == None):
            return
        else:
            # Current will point to head
            current = self.head
            while (current.next != None):
                # Index will point to node next to current
                index = current.next
                while (index != None):
                    # If current's data is greater than index's data, swap the data of current and index
                    if (current.score > index.score):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

                # display() will print out the nodes of the list

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.data),
            current = current.next

        print()


players_list = SortList()
length = int(input("Enter number of players : "))
for i in range(length):
    name = input("Input player's name : ")
    score = int(input("Input player's score : "))
    player = Node((name, score))
    players_list.addNode((name, score))
players_list.display()
print("\n \nAfter")

# Displaying original list
print("Original list: ")
players_list.display()

# Sorting list
players_list.sortList()

# Displaying a sorted list

print("Sorted list: ")
players_list.display()