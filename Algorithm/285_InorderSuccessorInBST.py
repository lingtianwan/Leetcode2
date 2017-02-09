# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor in the tree, return null.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        node = root
        succ = None
        while node:
            if p.val < node.val:
                succ = node
                node = node.left
            elif p.val > node.val:
                node = node.right
            else:
                break
        return succ
