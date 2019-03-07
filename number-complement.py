# https://leetcode.com/problems/number-complement/

num = 5

class Solution:
    def findComplement(self, num: int) -> int:
    	bin_num = str(bin(num)[2:])
    	complement_num = ""
    	for i in bin_num:
    		if i == "0":
    			complement_num += "1"
    		else:
    			complement_num += "0"
    	return int(complement_num, 2)



solution = Solution()
print(solution.findComplement(num))