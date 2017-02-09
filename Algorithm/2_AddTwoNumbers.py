# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = ListNode(0)
        cur = res
        while l1 and l2:
            cur.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            cur = cur.next
            l1 = l1.next
        while l2:
            cur.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            cur = cur.next
            l2 = l2.next
        if carry != 0:
            cur.next = ListNode(carry)
        return res.next
