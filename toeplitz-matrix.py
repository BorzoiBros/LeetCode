# https://leetcode.com/problems/toeplitz-matrix

# https://leetcode.com/problems/toeplitz-matrix/discuss/250081/Python-easily-understandable-beats-100-and-Average-O(n*m)-time-and-O(1)-space

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Get the rows of the matrix
        rows = len(matrix)
        # Get the columns of matrix by checking the number of items at first item in the matrix

        columns = len(matrix[0])
        boolean = True
        for col in range(columns):
        	i = 0
        	j = col
        	temp = matrix[i][j]
        	while i < rows and j < columns:
        		if matrix[i][j] != temp:
        			boolean = False
        		if boolean == False:
        			break
        		i += 1
        		j += 1

        	if boolean == False:
        		break
        if boolean:
        	for row in range(1, rows):
        		i = row
        		j = 0
        		temp = matrix[i][j]
        		while i < rows and j < columns:
        			if matrix[i][j] != temp:
        				boolean False
        			if boolean == False:
        				break
        			i += 1
        			j += 1
        		if boolean == False:
        			break
        	return boolean