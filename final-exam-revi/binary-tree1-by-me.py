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

    def find(self, in_user):
        return self.__find_node(self.root, in_user)

    def __find_node(self, node, in_user):
        if node is None:
            return False
        if node.username == in_user:
            return True
        left_node = self.__find_node(node.left, in_user)
        if left_node:
            return True
        return self.__find_node(node.right, in_user)

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
            val = successor.username
            self.__remove_node(node, successor.username)
            cur.username = val

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

    def preorder(self, node):
        if node is None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def inorder(self, node):
        if node is None:
            return
        self.preorder(node.left)
        print(node.data)
        self.preorder(node.right)


def start():
    tree = BST()
    tree.insert(Node("Nata", "nata11"))
    tree.insert(Node("Mill", "mill11"))
    tree.insert(Node("Foam", "foam11"))
    tree.insert(Node("Ton", "ton11"))
    tree.insert(Node("Zebea", "kung11"))
    tree.insert(Node("Guy", "Guy11"))
    tree.insert((Node("Amy", 'Amy11')))
    tree.insert((Node("Q", "efw1")))
    tree.insert((Node("P", "eff")))
    # tree.print_nodes(tree.root)
    tree.print_tree(tree.root, 0)
    print("********************************************************")
    # print(tree.find("Ton"))
    # print(tree.is_empty())
    # tree.remove("Guy")
    tree.print_tree(tree.root, 0)
    print("********************************************************")
    # tree.preorder(tree.root)
    tree.postorder(tree.root)


start()
