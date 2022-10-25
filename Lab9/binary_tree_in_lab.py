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

    def preorder(self, node):
        if node is None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

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


def start_7():
    tree = BST()
    for x in range(len(users7_pass)):
        tree.insert(Node(users7_pass[x][0], users7_pass[x][1]))
    choice = input("print : P\n"
                   "find user : F\n"
                   "remove : R\n"
                   "is empty? : E\n"
                   "print preorder : PO\n"
                   "print inorder : IO\n"
                   "print postorder : SO\n")
    if choice == "P":
        tree.print2D(tree.root)
    elif choice == "R":
        tree.print2D(tree.root)
        tree.remove("panya")
        print("\nAfter\n")
        tree.print2D(tree.root)
    elif choice == "F":
        print(tree.find("panya"))
    elif choice == "E":
        tree.is_empty()
    elif choice == "PO":
        tree.preorder(tree.root)
    elif choice == "IO":
        tree.inorder(tree.root)
    elif choice == "SO":
        tree.postorder(tree.root)
    else:
        print("Invalid input")


def start_1000():
    tree = BST()
    for x in range(len(users1000_pass)):
        tree.insert(Node(users1000_pass[x][0], users1000_pass[x][1]))
    choice = input("print : P\n"
                   "find user : F\n"
                   "remove : R\n"
                   "is empty? : E\n"
                   "print preorder : PO\n"
                   "print inorder : IO\n"
                   "print postorder : SO\n")
    if choice == "P":
        tree.print2D(tree.root)
    elif choice == "R":
        tree.print2D(tree.root)
        tree.remove("cat")
        print("\nAfter\n")
        tree.print2D(tree.root)
    elif choice == "F":
        print(tree.find("eve"))
    elif choice == "E":
        tree.is_empty()
    elif choice == "PO":
        tree.preorder(tree.root)
    elif choice == "IO":
        tree.inorder(tree.root)
    elif choice == "SO":
        tree.postorder(tree.root)
    else:
        print("Invalid input")


start_7()

