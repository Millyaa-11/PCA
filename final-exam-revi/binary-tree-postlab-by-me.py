file_7 = open("users7.txt").read().splitlines()
file_7_users = []
for i in file_7:
    file_7_users.append(i.split(" "))


class Node:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = (username, password)
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.__insert(self.root, new_node)

    def __insert(self, current_node, new_node):
        if new_node.username <= current_node.username:
            if current_node.left is not None:
                self.__insert(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.username > current_node.username:
            if current_node.right is not None:
                self.__insert(current_node.right, new_node)
            else:
                current_node.right = new_node

    def print_nodes(self, node):
        if node is None:
            return
        self.print_nodes(node.right)
        print(node.data)
        self.print_nodes(node.left)

    def print_tree(self, node, space):
        if node is None:
            return
        space += 10
        self.print_tree(node.right, space)
        print()
        for i in range(10, space):
            print(end=" ")
        print(node.data)
        self.print_tree(node.left, space)

    def find_user(self, in_user):
        return self.__find_user(self.root, in_user)

    def __find_user(self, node, in_user):
        if node is None:
            return False
        if node.username == in_user:
            return True
        left_node = self.__find_user(node.left, in_user)
        if left_node:
            return True
        return self.__find_user(node.right, in_user)

    def find_node(self, node, in_user, in_pass):
        if node is None:
            return False
        if node.username == in_user and node.password == in_pass:
            return True
        left_node = self.find_node(node.left, in_user, in_pass)
        if left_node:
            return True
        return self.find_node(node.right, in_user, in_pass)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def min_value_node(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur.data

    def remove(self, in_user):
        if self.root is None:
            return
        return self.__remove_node(self.root, in_user)

    def __remove_node(self, node, in_user):

        parent = None
        cur = node
        while cur.username != in_user:
            parent = cur
            if in_user < cur.username:
                cur = cur.left
            elif in_user > cur.username:
                cur = cur.right
        if cur is None:
            return

        # no children
        if cur.left is None and cur.right is None:
            if cur != node:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None

        # 2 children
        if cur.left is not None and cur.right is not None:
            # find successor
            successor = self.min_value_node(cur.right)
            val = successor
            self.__remove_node(node, successor)
            cur = val

        # 1 children
        else:
            if cur.left:
                child = cur.left
            else:
                child = cur.right

            if cur != node:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
            else:
                node = child
        return node

    def trim(self, min, max, node):
        if node is None:
            return
        node.left = self.trim(min, max, node.left)
        node.right = self.trim(min, max, node.right)
        if node.username > max:
            return node.left
        elif node.username < min:
            return node.right
        return node

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


def start():
    tree = BST()
    for i in file_7_users:
        tree.insert(Node(i[0], i[1]))
    choice = input("login : l\n trim : t\nInput choice : ")
    if choice == "l":
        x = 0
        username = input("Input username : ")
        password = input("Input password : ")
        while x in range(2) and tree.find_node(tree.root, username, password) is False:
            print("Password or Username incorrect")
            username = input("Input username : ")
            password = input("Input password : ")
            x += 1
        if tree.find_node(tree.root, username, password) is False:
            if tree.find_user(username):
                print("You have been removed")
                if username == tree.root.username:
                    tree.print_tree(tree.root.right, 0)
                    tree.print_tree(tree.root.left, 0)
                else:
                    tree.remove(username)
                    tree.print_tree(tree.root, 0)
            else:
                print("Username does not exist")
        else:
            print("You are logged in")
    if choice == "t":
        tree.print_tree(tree.root, 0)
        print("***********************************************************************")
        tree.trim("prim", "tisha", tree.root)
        if tree.root.username < "prim" or tree.root.username > "tisha":
            tree.root = tree.remove(tree.root.username)
        tree.print_tree(tree.root, 0)
    if choice == "c":
        print(tree.count_nodes(tree.root))


start()
