# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/233386/python-easy-solution

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root:
            while root.children:
            	tmp = root.children.pop(0)
            	result += self.postorder(tmp)
            result.append(root.val)
        return result