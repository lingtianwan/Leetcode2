# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        k = len(primes)
        p = [0 for _ in range(k)]
        i = 1
        while i < n:
            m = [0 for _ in range(k)]
            for j in range(k):
                m[j] = res[p[j]] * primes[j]
            minval = min(m)
            res.append(minval)
            for j in range(k):
                if m[j] == minval:
                    p[j] += 1
            i += 1
        return res[-1]
