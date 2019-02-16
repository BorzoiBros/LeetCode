class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for letter in S:
            if letter in J:
                count += 1
        return count
        

A = "z"
B = "ZZ"

solution = Solution()
print(solution.numJewelsInStones(A,B))
