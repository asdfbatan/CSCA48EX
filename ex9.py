class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as d value of 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0  # just a variable that we may want to set later

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""
        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        self.d = depth
        if self.right is not None:
            self.right.set_depth(depth+1)
        if self.left is not None:
            self.left.set_depth(depth+1)

    def leaves_and_internals(self):
        leaves, internals = set(), set()
        if self.right is not None and self.left is not None:
            leaves_l, internals_l = BTNode._helper(self.left)
            leaves_r, internals_r = BTNode._helper(self.right)
            leaves, internals = leaves_l.union(leaves_r),
            internals_l.union(internals_r)
            return leaves, internals

    def _helper(node):
        leaves, internals = set(), set()
        if node is not None:
            leaves_l, internals_l = BTNode._helper(node.left)
            leaves_r, internals_r = BTNode._helper(node.right)
            leaves, internals = leaves_l.union(leaves_r),
            internals_l.union(internals_r)
            if node.right is None and node.left is None:
                leaves.add(node.value)
            else:
                internals.add(node.value)
        return leaves, internals

    def sum_to_deepest(self):
        return BTNode._sum_helper(self, 0, 0)[1]

    def _sum_helper(node, depth, sum):
        if node is None:
            return (depth, sum)
        return max(BTNode._sum_helper(node.right, depth + 1, sum + node.value),
                   BTNode._sum_helper(node.left, depth + 1, sum + node.value))

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
