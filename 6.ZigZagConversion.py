# https://leetcode.com/problems/zigzag-conversion/


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        start = 0
        count = 0
        weird = 1
        increment = 2*(numRows-1)
        final = ""
        n = len(s)
        while True:
            final = final + s[start]
            if count == 0 or count == numRows - 1:
                start += increment
            else:
                if weird == 0:
                    start += start + increment - (start + increment - 2 * count)
                    weird = 1
                elif weird == 1:
                    start += increment - 2 * count
                    weird = 0
            if start >= n:
                start = 0
                count += 1
                start += count
                weird = 1
            if len(final) == n:
                break
        return final
