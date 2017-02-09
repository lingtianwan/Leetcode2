# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.num_map = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.num_map[number] = self.num_map.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.num_map.keys():
            j = value - i
            if (j == i and self.num_map[j] > 1) or (j != i and j in self.num_map):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
