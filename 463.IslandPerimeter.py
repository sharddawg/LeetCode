# https://leetcode.com/problems/island-perimeter/


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n1 = len(grid)
        n2 = len(grid[0])
        totalcount = 0
        for i in range(n1):
            for j in range(n2):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    count = 4
                    if i != 0:
                        if grid[i-1][j] == 1:
                            count -= 1
                    if i!= n1-1:
                        if grid[i+1][j] == 1:
                            count -= 1
                    if j != 0:
                        if grid[i][j-1] == 1:
                            count -= 1
                    if j != n2-1:
                        if grid[i][j+1] == 1:
                            count -= 1
                    totalcount += count
        return totalcount
