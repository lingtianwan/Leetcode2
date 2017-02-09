# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Hint:
#
# No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
# Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
# Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator / denominator)
        sign = 1
        if numerator * denominator < 0:
            sign = -1
        numer = abs(numerator)
        denom = abs(denominator)
        remain = {}
        res = str(numer / denom) + '.'
        numer = (numer % denom) * 10
        num_list = []
        cnt = 0
        repeat = ''
        while True:
            cur = numer / denom
            mod = numer % denom
            if numer in remain:
                repeat = ''.join(num_list[remain[numer]:cnt])
                break
            else:
                num_list.append(str(cur))
                remain[numer] = cnt
                if numer % denom == 0:
                    break
                else:
                    numer = (numer % denom) * 10
                    cnt += 1
        if repeat == '':
            res += ''.join(num_list)
        else:
            res += ''.join(num_list[:remain[numer]]) + '(' + repeat + ')'
        if sign == -1:
            res = '-' + res
        return res
