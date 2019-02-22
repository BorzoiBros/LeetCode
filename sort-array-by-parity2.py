# https://leetcode.com/problems/sort-array-by-parity-ii/

A = [4,2,5,7]

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for index, value in enumerate(odd):
            even.insert(index * 2 + 1, value)
        return even

solution = Solution()
print(solution.sortArrayByParityII(A))



