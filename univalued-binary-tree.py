# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

x = [1,1,1,1,1,null,1]

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root = x[0]
        for i in x:
            if i == x or i == null:
                continue
            else:
                return False
        return True

solution = Solution()
print(solution.isUnivalTree(x))

