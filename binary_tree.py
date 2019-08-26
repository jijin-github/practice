class NewNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def topViewDetails(root, m, hd, level):
    if not root:
        return
    if hd in m:
        if level < m[hd][1]:
            m.update({hd: [root.data, level]})
    else:
        m[hd] = [root.data, level]

    topViewDetails(root.left, m, hd - 1, level + 1)
    topViewDetails(root.right, m, hd + 1, level + 1)

def printTopbinary(root):
    m = {}
    topViewDetails(root, m, 0, 0)
    for key, value in m.iteritems():
        print value[0],

root = NewNode(1)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.right = NewNode(4)
root.left.right.right = NewNode(5)
root.left.right.right.right = NewNode(6)
printTopbinary(root)



