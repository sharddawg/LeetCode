# https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums_dict = {}
        duplicates = {}
        for i in range(n):
            nums_dict[nums[i]] = i
        result = []
        for i in range(n):
            for j in range(i+1, n):
                s = -(nums[i] + nums[j])
                if s in nums_dict and nums_dict[s] != i and nums_dict[s] != j:
                    in_order = sorted([nums[i], nums[j], s])
                    tuple_in_order = tuple(in_order)
                    if tuple_in_order not in duplicates:
                        result.append(in_order)
                        duplicates[tuple_in_order] = 1
                
        return result
