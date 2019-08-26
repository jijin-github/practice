class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def top_view(root, m, hd, level):
    if not root:
        return
    if hd in m:
        if level < m[hd][1]:
            m.update( {hd : [root.data, level] })
    else:
        m[hd] = [root.data, level]

    top_view(root.left, m, hd - 1, level + 1)
    top_view(root.right, m, hd + 1, level + 1)

def print_top_view(root):
    m = {}
    top_view(root, m, 0, 0)
    print(m,"<<<<<<<<<")
    for key, value in m.iteritems():
        print value[0],

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print_top_view(root)