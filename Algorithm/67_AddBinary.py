# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#
# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        res = ''
        for i in range(max_len - 1, -1, -1):
            sums = int(a[i]) + int(b[i]) + carry
            if sums < 2:
                res += str(sums)
                carry = 0
            elif sums == 2:
                res += '0'
                carry = 1
            else:
                res += '1'
                carry = 1
        if carry == 1:
            res += '1'
        return res[::-1]
