# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        mult = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                mult[i + j] += int(num1[i]) * int(num2[j])
        carry = 0
        res = ''
        for i in range(len(mult)):
            digit = (mult[i] + carry) % 10
            carry = (mult[i] + carry) / 10
            res += str(digit)
        if carry > 0:
            res += str(carry)[::-1]
        res = res[::-1]
        while len(res) > 1 and res[0] == '0':
            res = res[1:]
        return res
