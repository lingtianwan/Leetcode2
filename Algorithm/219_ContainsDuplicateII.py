# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map and i - hash_map[num] <= k:
                return True
            else:
                hash_map[num] = i
        return False
