##Given an array of integers A sorted in non-decreasing order,
##return an array of the squares of each number, 
##also in sorted non-decreasing order.
##
## 
##
##Example 1:
##
##Input: [-4,-1,0,3,10] Output: [0,1,9,16,100] 
##
##Example 2:
##
##Input: [-7,-3,2,3,11] Output: [4,9,9,49,121] 
##
## 
##
##Note:
##
##1 <= A.length <= 10000
##
##-10000 <= A[i] <= 10000
##
##A is sorted in non-decreasing order.
##
A = [-4,-1,0,3,10]

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        neg = []
        pos = []
        for i in range(len(A)):
            if A[i] < 0:
                neg.append(A[i]*A[i])
            else:
                pos.append(A[i]*A[i])
        print("neg is",neg)
        print("pos is",pos)
        j = len(pos)
        if j == 0:
            for k in reversed(neg):
                pos.append(k)
        else:
            for k in neg:
                while j > 0:
                    print("k is",k)
                    print("pos[j-1] is",pos[j-1])
                    if k < pos[0]:
                        pos.insert(0,k)
                        break
                    elif k >= pos[j-1]:
                        pos.insert(j,k)
                        break
                    else:
                        j -= 1
               
                    
        return pos

solution = Solution()
print(solution.sortedSquares(A))
