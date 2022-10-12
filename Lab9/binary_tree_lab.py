import os

users1000 = users1000.txt()

class Node:
    def __init__(self, username_in, password_in):
        # your code here
        self.username = username_in
        self.password = password_in
        self.data = (username_in, password_in)
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if new_node.username <= current_node.username:
            if current_node.left is not None:
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.username > current_node.username:
            if current_node.right is not None:
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find(self, username):
        return self.__find_node(self.root, username)

    def __find_node(self, current_node, username):
        while username != current_node:
            lside = __find_node(current_node.left, username)
            rside = __find_node(current_node.right, username)
            if username < current_node.left:
                lside + 1
            if username > current_node.right:
                rside + 1
        return current_node.data

    # your code here

    #def remove(self, username):

    # your code here

    #def is_empty(self):

    # your code here

    #def preorder(self):

    # your code here

    #def inorder(self):

    # your code here

    #def postorder(self):

    # your code here

    #def print(self):


def start():
    account_tree = BST()
    num = int(input("Input number of nodes : "))
    for i in range (num):
        user = int(input("Enter username : "))
        passw = input("Enter password : ")
        account_tree.insert(Node(user,passw))


start()