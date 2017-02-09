# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return collections.Counter(bin(n)[2:])['1']

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        x = 2 ** 32
        while x > 0:
            if n // x != 0:
                cnt += 1
                n %= x
            x /= 2
        return cnt + n
