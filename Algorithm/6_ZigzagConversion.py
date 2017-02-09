# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        hold = ['' for i in range(numRows)]
        step = 0
        down = 1
        for i in range(len(s)):
            hold[step] += s[i]
            if down == 1:
                if step + 1 == numRows:
                    step -= 1
                    down = 0
                else:
                    step += 1
            else:
                if step == 0:
                    step += 1
                    down = 1
                else:
                    step -= 1
        res = ''
        for elem in hold:
            res += elem
        return res
