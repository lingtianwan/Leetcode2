# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while carry > 0 and i >= 0:
            digit = digits[i] + 1
            if digit > 9:
                carry = digit / 10
                digit = digit % 10
            else:
                carry = 0
            digits[i] = digit
            i -= 1
        if carry > 0:
            digits.insert(0, carry)
        return digits
