#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
#Given two integers x and y, calculate the Hamming distance.
#
#Note:
#0 ≤ x, y < 231.
#
#Example:
#
#Input: x = 1, y = 4
#
#Output: 2
#
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑
#
#The above arrows point to positions where the corresponding bits are different.

x = 1
y = 4
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        maxlen = 0
        if abs(y) > x:
            maxlen = len(bin(y)[2:])
        else:
            maxlen = len(bin(x)[2:])

        x_bin = bin(x)[2:].zfill(maxlen)
        y_bin = bin(y)[2:].zfill(maxlen)
        print(x_bin)
        print(y_bin)
        difference = 0
        for i in range(maxlen):
            if x_bin[i] != y_bin[i]:
                difference += 1
            else:
                continue
        return difference


solution = Solution()
print(solution.hammingDistance(x,y))
