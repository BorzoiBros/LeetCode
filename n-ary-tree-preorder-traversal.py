# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/233385/python-easy-solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root:
        	result.append(root.val)
        	while root.children:
        		tmp = root.children.pop(0)
        		result += self.preorder(tmp)
        return result