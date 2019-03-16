# https://leetcode.com/problems/toeplitz-matrix

# https://leetcode.com/problems/toeplitz-matrix/solution/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for r, row in enumerate(matrix):
        	for c, val in enumerate(row):
        		if r-c not in groups:
        			groups[r-c] = val
        		elif groups[r-c] != val:
        			return False
        return True