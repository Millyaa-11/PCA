class Node:
    def __init__(self, data):
        self.data = data
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
        if new_node.data <= current_node.data:
            if current_node.left is not None:
                self.__insert(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.data > current_node.data:
            if current_node.right is not None:
                self.__insert(current_node.right, new_node)
            else:
                current_node.right = new_node

    def print_nodes(self, node):
        if node is None:
            return
        self.print_nodes(node.left)
        print(node.data)
        self.print_nodes(node.right)

    def find(self, data):
        return self.__find_node(self.root, data)

    def __find_node(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        left_search = self.__find_node(node.left, data)
        if left_search:
            return True
        return self.__find_node(node.right, data)

    def find_min_val(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def remove(self, data):
        if self.root is None or self.find(data) is False:
            return
        return self.__remove__(self.root, data)

    def __remove__(self, node, data):
        parent = None
        cur = node
        while cur.data != data:
            parent = cur
            if data < cur.data:
                cur = cur.left
            elif data > cur.data:
                cur = cur.right
        if cur is None:
            return
        # no child
        if cur.left is None and cur.right is None:
            if cur != node:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node = None
        # 2 child
        if cur.left is not None and cur.right is not None:
            successor = self.find_min_val(node.right)
            val = successor.data
            self.__remove__(node, successor.data)
            cur.data = val
        # 1 child
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

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def print_tree(self, node, space):
        if node is None:
            return
        space += 10
        self.print_tree(node.right, space)
        for i in range(10, space):
            print(end=" ")
        print(node.data)
        self.print_tree(node.left, space)


    def pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    def node_counts(self, node):
        if node is None:
            return 0
        return self.node_counts(node.left) + self.node_counts(node.right) + 1

    def trim(self, min, max, node):
        if node is None:
            return
        node.left = self.trim(min, max, node.left)
        node.right = self.trim(min, max, node.right)
        if node.data < min:
            return node.right
        elif node.data > max:
            return node.left
        return node

    def pop(self, node):
        if node is None:
            return

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def perc_up(self, i):
        # until root
        while i // 2 > 0:
            # if child < parent -> swap
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            # go to upper parent
            i = i // 2

    def perc_down(self, i):
        # until last level
        while i * 2 <= self.current_size:
            mc = self.minChild(i)
            # if current node > minChild -> swap
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        # if not have left child return root
        if i * 2 + 1 > self.current_size:
            return i * 2
        # have child
        else:
            # if parent < left child : return parent
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # find the smallest item in tree del and restore tree
        # 1. take last item and move to root
        # 2. push new root (that we just swap) down to where it should be in tree
        retvel = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size = self.current_size - 1
        self.heapList.pop()
        self.perc_down(1)
        return retvel


def start():
    tree = BST()
    tree.insert(Node(6))
    tree.insert(Node(2))
    tree.insert(Node(3))
    tree.insert(Node(4))
    tree.insert(Node(1))
    tree.insert(Node(10))
    tree.insert(Node(8))
    # tree.print_nodes(tree.root)
    # tree.remove(7)
    # tree.print_nodes(tree.root)
    # print(tree.is_empty())
    # tree.pre_order(tree.root)
    # tree.in_order(tree.root)
    # tree.post_order(tree.root)
    # tree.print_tree(tree.root, 0)
    # print(tree.node_counts(tree.root))
    tree.print_tree(tree.root, 0)
    print("**************************************************************")
    tree.trim(7, 10, tree.root)
    if tree.root.data < 7 or tree.root.data < 8:
        tree.root = tree.remove(tree.root.data)
    tree.print_tree(tree.root, 0)

start()
