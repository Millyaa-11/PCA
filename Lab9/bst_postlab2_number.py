class Node:
    def __init__(self, num):
        self.num = num
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
        if new_node.num <= current_node.num:
            if current_node.left is not None:
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.num > current_node.num:
            if current_node.right is not None:
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def minValueNode(self, node):
        current = node
        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current

    def remove(self, num):
        if self.root is None:
            return
        else:
            return self.__remove(self.root, num)

    def __remove(self, node, find_num):
        # Function to delete a node from a BST

        # pointer to store the parent of the current node
        parent = None

        # start with the root node
        curr = node

        # search key in the BST and set its parent pointer
        while curr and curr.num != find_num:
            parent = curr
            if find_num < curr.num:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return node

        # Case 1: node to be deleted has no children, i.e., it is a leaf node
        if curr.left is None and curr.right is None:
            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None

        # Case 2: node to be deleted has two children
        elif curr.left and curr.right:

            # find its inorder successor node
            successor = self.minValueNode(curr.right)

            # store successor value
            val = successor.num

            # recursively delete the successor. Note that the successor
            # will have at most one child (right child)
            self.__remove(node, successor.num)

            # copy value of the successor to the current node
            curr.num = val

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
        for p in range(10, space):
            print(end=" ")
        print(node.num)

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
        if node.num < btw[0]:
            child_right = node.right
            return child_right
        elif node.num > btw[1]:
            child_left = node.left
            return child_left
        return node


def start():
    tree = BST()
    tree.insert(Node(8))
    tree.insert(Node(3))
    tree.insert(Node(1))
    tree.insert(Node(6))
    tree.insert(Node(4))
    tree.insert(Node(7))
    tree.insert(Node(10))
    tree.insert(Node(14))
    tree.insert(Node(13))
    tree.print2D(tree.root)
    tree.trim((5, 13), tree.root)
    print("\n", "*" * 20, "After", "*" * 20)
    tree.print2D(tree.root)

start()
