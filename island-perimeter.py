# https://leetcode.com/problems/island-perimeter/
# https://leetcode.com/problems/island-perimeter/discuss/95003/Easy-to-read-Python-solution

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        """
        if not grid:
        	return 0

        def sum_adjacent(i, j):
        	adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
        	res = 0
        	for x, y in adjacent:
        		if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
        			res += 1
        	return res
  	    count = 0
    	  for i in range(len(grid)):
      		for j in range(len(grid[0])):
      			if grid[i][j] == 1:
      				count += sum_adjacent(i, j)
      	return count

solution = Solution()
print(solution.islandPerimeter(grid))