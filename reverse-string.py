# https://leetcode.com/problems/reverse-string/

s = ["h","e","l","l","o"]

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        insert_idx = len(s) -1
        while insert_idx > 0:
        	s.insert(insert_idx, s.pop(0))
        	insert_idx -= 1
        	print(s)



solution = Solution()
solution.reverseString(s)