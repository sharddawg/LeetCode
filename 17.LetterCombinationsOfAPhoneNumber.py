# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        table = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        result = []
        queue = []
        queue.append("")
        while len(queue) > 0:
            s = queue.pop(0)
            if len(s) == len(digits):
                result.append(s)
            else:
                for letter in table[int(digits[len(s)])]:
                    queue.append(s+letter)
        return result
        
