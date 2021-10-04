# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i, num in enumerate(nums):
            rem = target-num
            if rem in dictionary:
                return [dictionary[rem], i]
            dictionary[num] = i
        return None
