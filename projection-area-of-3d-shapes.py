# https://leetcode.com/problems/projection-area-of-3d-shapes/
# https://leetcode.com/problems/projection-area-of-3d-shapes/discuss/156726/C%2B%2BJavaPython-Straight-Forward

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(v > 0 for row in grid for v in row)
