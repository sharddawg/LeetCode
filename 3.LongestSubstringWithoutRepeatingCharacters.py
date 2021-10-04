class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dict = {}
        i = 0
        j = 0
        maximum = 0
        lengths = [0]
        while j < n:
            if s[j] not in dict:
                dict[s[j]] = 1
                maximum += 1
                j += 1
            else:
                lengths.append(maximum)
                maximum = 0
                i += 1
                j = i
                dict = {}
        return max(max(lengths), maximum)
