# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Hint:
#
# Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
# Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
# There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = ''
        billion = num / 1000000000
        if billion != 0:
            res += self.helper(billion) + ' Billion '
        num %= 1000000000
        million = num / 1000000
        if million != 0:
            res += self.helper(million) + ' Million '
        num %= 1000000
        thousand = num / 1000
        if thousand != 0:
            res += self.helper(thousand) + ' Thousand '
        num %= 1000
        res += self.helper(num)
        if len(res) > 0 and res[-1] == ' ':
            res = res[:-1]
        return res



    def helper(self, num):
        ones = {
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine'
                }
        tens = {
                2:'Twenty',
                3:'Thirty',
                4:'Forty',
                5:'Fifty',
                6:'Sixty',
                7:'Seventy',
                8:'Eighty',
                9:'Ninety',
                10:'Ten',
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen'
                }
        res = ''
        if num / 100:
            res += ones[num / 100] + ' Hundred '
        num %= 100
        ten = num / 10
        if ten == 1:
            res += tens[num]
            return res
        elif ten != 0:
            res += tens[ten] + ' '
        num %= 10
        if num != 0:
            res += ones[num]
        if len(res) > 0 and res[-1] == ' ':
            res = res[:-1]
        return res
