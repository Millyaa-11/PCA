class Node:

# create node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# find dept of node
def Depth(node):
    if node is None:
        return 0
    else:
        # recursive will loop until the end of dept
        lDepth = Depth(node.left)
        rDepth = Depth(node.right)
        # compare left and right dept to find the deepest dept
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


def TotalNodes(root):
    if root == None:
        return 0
    lh = left_height(root)
    rh = right_height(root)
    if lh == rh:
        return (1 << lh) - 1
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


def printLeafNodes(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.data)
        return
    if root.left:
        printLeafNodes(root.left)
    if root.right:
        printLeafNodes(root.right)



def start():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print("Height of tree is %d" % (Depth(root)))

start()