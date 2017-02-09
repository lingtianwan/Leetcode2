# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if not (node1 or node2):
                continue
            if (not node1) or (not node2) or (node1.val != node2.val):
                return False
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, root)

    def check(self, node1, node2):
        if not (node1 or node2):
            return True
        if (not node1) or (not node2) or (node1.val != node2.val):
            return False
        return self.check(node1.left, node2.right) and self.check(node1.right, node2.left)
