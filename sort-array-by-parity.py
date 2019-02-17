#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
#You may return any answer array that satisfies this condition.
#Example 1:
#
#Input: [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
#
#Note:
#
#1 <= A.length <= 5000
#0 <= A[i] <= 5000
#https://leetcode.com/problems/sort-array-by-parity/

A = [3,1,2,4]
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_sorted = []
        for i in A:
            if i % 2 == 0:
#                print(i, "is even number")
                A_sorted.insert(0,i)
            else:
#                print(i, "is odd number")
                A_sorted.insert(len(A_sorted),i)
        return A_sorted
solution = Solution()
print(solution.sortArrayByParity(A))
