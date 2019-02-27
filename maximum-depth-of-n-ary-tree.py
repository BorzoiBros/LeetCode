# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/discuss/245157/Python-solution-faster-than-99.80
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/discuss/151804/Solution-Python-C%2B%2B-Simple-with-explanation
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # if not root:
        #     return 0
        # depth = 1
        # current_level = [root]
        # while current_level:
        #     next_level = []
        #     for node in current_level:
        #         if node.children:
        #             next_level.extend(node.children)
        #     if next_level:
        #         depth += 1
        #         current_level = next_level
        #     else:
        #         break
        # return depth
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1