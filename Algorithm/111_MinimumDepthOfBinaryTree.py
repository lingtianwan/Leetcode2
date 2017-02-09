# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node, d):
            if not (node.left or node.right):
                return d
            left = right = 2147483647
            if node.left:
                left = depth(node.left, d + 1)
            if node.right:
                right = depth(node.right, d + 1)
            return min(left, right)
        if not root:
            return 0
        return depth(root, 1)
