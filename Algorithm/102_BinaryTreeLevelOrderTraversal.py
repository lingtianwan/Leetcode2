# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def traversal(node, depth):
            if not node:
                return
            if depth > len(res) - 1:
                res.append([node.val])
            else:
                res[depth].append(node.val)
            traversal(node.left, depth+1)
            traversal(node.right, depth+1)
        res = []
        traversal(root, 0)
        return res
