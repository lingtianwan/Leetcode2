# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def dfs(node, path):
            if node.left is None and node.right is None:
                res.append(path)
                return
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))
        res = []
        if root is None:
            return []
        dfs(root, str(root.val))
        return res
