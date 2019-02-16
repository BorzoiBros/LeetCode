J = "aA"
S = "aAAbbbb"

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            if i in J:
                count += 1
            else:
                continue
        return count

solution = Solution()
print(solution.numJewelsInStones(J,S))
