class Tree(object):

    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not(self.left or self.right)

    def __str__(self):
        if self.is_leaf(): return '[%s]' % (str(self.root)+':'+str(self.root.weight))
        return '[%s %s %s]' % ('_' if self.left is None else str(self.left),
        str(self.root.value)+':'+str(self.root.weight), '_' if self.right is None else str(self.right))

    def __eq__(self, other):
        if self is None or other is None: return self is None and other is None
        return ((self.root.value == other.root.value)and
        (self.left == other.left)and(self.right == other.right))

    def __ne__(self, other):
        if self is None or other is None: return self is not None or other is not None
        return ((self.root.value != other.root.value)or
        (self.left.__ne__(other.left))or(self.right.__ne__(other.right)))

class Node(object):

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

def cost(tree, depth=1):
    '''
    Returns the cost of a tree which root is depth deep.
    '''
    if tree is None: return 0
    if tree.is_leaf(): return tree.root.weight * depth
    return tree.root.weight * depth + cost(tree.left, depth + 1) + cost(tree.right, depth + 1)

def make_min_tree(node_list):
    '''
    node_list is a list of Node objects
    Pre-cond: len(node_list > 0) and node_list is sorted in ascending order
    Returns a minimal cost tree of all nodes in node_list.
    '''
    # segments[n][i] finds the root for min tree consisting of nodes node_list[i:i+n+1]
    # segments[n][i] contains the index, reffering to the root; the cost of the min tree;
    #                and the sum of the weights of its nodes
    # segments[n][i] = [k,cost,weight]
    # segments will be found dynamically, starting with segments of length 0

    segments = list()
    m = len(node_list)
    for i in range(0,m): segments.append([[0,0,0]]*(m-i))
    for i in range(0,m): segments[0][i] = [i,node_list[i].weight,node_list[i].weight]
    for n in range(1,m):
        for i in range(0,m-n): #finding segments[n][i]
            argmin = None
            mincost = None
            for k in range(i,i+n+1):
                cost = (node_list[k].weight +
                (0 if k == i else (segments[k-i-1][i][1] + segments[k-i-1][i][2])) +
                (0 if k == i+n else (segments[i+n-k-1][k+1][1] + segments[i+n-k-1][k+1][2])))
                if mincost is None or mincost > cost: argmin, mincost = k, cost
            k = argmin
            segments[n][i] = [argmin, mincost, node_list[k].weight +
            (0 if k == i else (segments[k-i-1][i][2])) +
            (0 if k == i+n else (segments[i+n-k-1][k+1][2]))]

    def build_tree(istart,length):
        iroot = segments[length][istart][0]
        return Tree(node_list[iroot],
        (None if iroot == istart else build_tree(istart, iroot - istart - 1)),
        (None if iroot == istart + length else build_tree(iroot + 1, istart + length - iroot - 1)))

    return build_tree(0,m-1)