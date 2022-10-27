users1000 = (open("users1000.txt")).read().splitlines()
users1000_pass = []
for i in range(len(users1000)):
    users1000_pass.append((users1000[i].split(" ")))

users7 = (open("users7.txt")).read().splitlines()
users7_pass = []
for i in range(len(users7)):
    users7_pass.append((users7[i].split(" ")))

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
        if self.root is None:
            return
        else:
            return self.__find_node(self.root, username)

    def __find_node(self, node, find_user):
        if node is None:
            return False
        if node.username == find_user:
            return True
        #  then recur on left subtree
        left_nodes = self.__find_node(node.left, find_user)
        if left_nodes:
            return True
        #  node is not found in left so recur on right subtree
        right_nodes = self.__find_node(node.right, find_user)
        return right_nodes

    def find_account(self, node, find_user, find_pass):
        if node is None:
            return False
        if node.data == (find_user, find_pass):
            return True
        left_nodes = self.__find_node(node.left, find_user)
        if left_nodes:
            return True
        #  node is not found in left so recur on right subtree
        right_nodes = self.__find_node(node.right, find_user)
        return right_nodes

    def minValueNode(self, node):
        current = node
        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current

    def remove(self, username):
        if self.root is None:
            return
        else:
            return self.__remove(self.root, username)

    def __remove(self, node, find_user):
        # Function to delete a node from a BST

        # pointer to store the parent of the current node
        parent = None

        # start with the root node
        curr = node

        # search key in the BST and set its parent pointer
        while curr and curr.username != find_user:

            # update the parent to the current node
            parent = curr

            # if the given key is less than the current node, go to the left subtree;
            # otherwise, go to the right subtree
            if find_user < curr.username:
                curr = curr.left
            else:
                curr = curr.right

        # return if the key is not found in the tree
        if curr is None:
            return node

        # Case 1: node to be deleted has no children, i.e., it is a leaf node
        if curr.left is None and curr.right is None:

            # if the node to be deleted is not a root node, then set its
            # parent left/right child to None
            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            # if the tree has only a root node, set it to None
            else:
                node = None

        # Case 2: node to be deleted has two children
        elif curr.left and curr.right:

            # find its inorder successor node
            successor = self.minValueNode(curr.right)

            # store successor value
            val = successor.username

            # recursively delete the successor. Note that the successor
            # will have at most one child (right child)
            self.__remove(node, successor.username)

            # copy value of the successor to the current node
            curr.username = val

        # Case 3: node to be deleted has only one child
        else:

            # choose a child node
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            # if the node to be deleted is not a root node, set its parent
            # to its child
            if curr != node:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            # if the node to be deleted is a root node, then set the root to the child
            else:
                node = child

        return node

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def print2D(self, root):
        self.print_tree(root, 0)

    def print_tree(self, node, space):
        # Base case
        if node is None:
            return
        # Increase distance between levels
        space += 10

        # Process right child first
        self.print_tree(node.right, space)
        # Print current node after space
        # count
        print()
        for p in range(10, space):
            print(end=" ")
        print(node.data)

        # Process left child
        self.print_tree(node.left, space)

    def TotalNodes(self, node):
        if node is None:
            return 0
        return 1 + self.TotalNodes(node.left) + self.TotalNodes(node.right)

    def trim(self, btw, node):
        # return if the key is not found in the tree
        if node is None:
            return
        node.left = self.trim(btw, node.left)
        node.right = self.trim(btw, node.right)
        if node.username < btw[0]:
            child_right = node.right
            return child_right
        elif node.username > btw[1]:
            child_left = node.left
            return child_left
        return node


def start_7():
    i = 0
    tree = BST()
    for x in range(len(users7_pass)):
        tree.insert(Node(users7_pass[x][0], users7_pass[x][1]))
    choice = input("login : L\n"
                   "count nodes : C\n"
                   "trim : T\n")
    if choice == "L":
        user_in = input("Input your username : ")
        pass_in = input("Input your password : ")
        while i in range(3) and tree.find_account(tree.root, user_in, pass_in) is False:
            print("Username doesn't exist\n")
            user_in = input("Input your username :")
            pass_in = input("Input your password : ")
            i += 1
        if tree.find_account(tree.root, user_in, pass_in) is False:
            print("You have been removed")
            exit(1)
        else:
            print("\nYou are now logged in")
    elif choice == "C":
        print(tree.TotalNodes(tree.root))
    elif choice == "T":
        min_name = input("Input the minimum username : ")
        max_name = input("\nInput the maximum username : ")
        btw = (min_name, max_name)
        tree.print2D(tree.root)
        tree.trim(btw, tree.root)
        print("\n", "*" * 20, "After", "*" * 20)
        tree.print2D(tree.root)


def start_1000():
    i = 0
    tree = BST()
    for x in range(len(users1000_pass)):
        tree.insert(Node(users1000_pass[x][0], users1000_pass[x][1]))
    choice = input("login : L\n"
                   "count nodes : C\n"
                   "trim : T\n")
    if choice == "L":
        user_in = input("Input your username : ")
        pass_in = input("Input your password : ")
        while i in range(3) and tree.find_account(tree.root, user_in, pass_in) is False:
            print("Username doesn't exist\n")
            user_in = input("Input your username :")
            pass_in = input("Input your password : ")
            i += 1
        if tree.find_account(tree.root, user_in, pass_in) is False:
            print("You have been removed")
            exit(1)
        else:
            print("\nYou are now logged in")
    elif choice == "C":
        print(tree.TotalNodes(tree.root))
    elif choice == "T":
        min_name = input("Input the minimum username : ")
        max_name = input("\nInput the maximum username : ")
        btw = (min_name, max_name)
        tree.print2D(tree.root)
        tree.trim(btw, tree.root)
        print("\n", "*" * 20, "After", "*" * 20)
        tree.print2D(tree.root)


start_7()

