class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = True
        while found:
          for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
          found = False
        return False
    
num_list = [1,3,3,5]

solution = Solution() 
solution_result = solution.twoSum(num_list,8)
print(solution_result)
