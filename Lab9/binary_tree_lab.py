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
        while (current.left is not None):
            current = current.left

        return current

    def remove(self, username):
        if self.root is None:
            return
        else:
            return self.__remove(self.root, username)

    def __remove(self, node, find_username):
        if node is None:
            return None
        else:
            # If the key to be deleted
            # is smaller than the root's
            # key then it lies in  left subtree
            if find_username < node.username:
                node.left = self.__remove(node.left, find_username)

            # If the kye to be delete
            # is greater than the root's key
            # then it lies in right subtree
            elif (find_username > node.username):
                node.right = self.__remove(node.right, find_username)

            # If key is same as root's key, then this is the node
            # to be deleted
            else:

                # Node with only one child or no child
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp

                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                # Node with two children:
                # Get the inorder successor
                # (smallest in the right subtree)
                temp = self.minValueNode(node.right)

                # Copy the inorder successor's
                # content to this node
                node.username = temp.username

                # Delete the inorder successor
                node.right = self.__remove(node.right, temp.username)
            return node.username

    #def is_empty(self):

    # your code here

    #def preorder(self):

    # your code here

    #def inorder(self):

    # your code here

    #def postorder(self):

    # your code here

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.root.right is None and self.root.left is None:
            line = '%s' % self.root.username
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.root.right is None:
            lines, n, p, x = self.root.left._display_aux()
            s = '%s' % self.root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.root.left is None:
            lines, n, p, x = self.root.right._display_aux()
            s = '%s' % self.root.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.root.left._display_aux()
        right, m, q, y = self.root.right._display_aux()
        s = '%s' % self.root.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def start():
    tree = BST()
    for x in range(len(users7_pass)):
        tree.insert(Node(users7_pass[x][0], users7_pass[x][1]))
    #  print(tree.find("dang"))
    print(tree.display())


start()
