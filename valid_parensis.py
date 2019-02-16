class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        OPENING_BRACKETS = {"{", "[", "("}
        BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}
        stack = []
        for bracket in s:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            elif not stack:
                return False # Can't pop from an empty stack
            elif stack.pop() != BRACKETS_MAP[bracket]:
                return False # Closing the wrong kind of bracket
        return not stack


solution = Solution()
print(solution.isValid("()[]{}"))
