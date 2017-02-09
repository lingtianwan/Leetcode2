# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findDepth(root, 0)

    def findDepth(self, node, depth):
        if node is None:
            return depth
        return max(self.findDepth(node.left, depth + 1), self.findDepth(node.right, depth + 1))
