# https://leetcode.com/problems/longest-palindromic-substring/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest = ""
        maximum = 0
        for i in range(n):
            splice = s[i:]
            while len(splice) > maximum:
                if splice == splice[::-1]:
                    if len(splice) > maximum:
                        longest = splice
                        maximum = len(splice)
                splice = splice[:-1]
        return longest
    
