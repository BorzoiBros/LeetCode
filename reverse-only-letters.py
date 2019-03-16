class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        characters = [c for c in S if c.isalpha()]
        S_list = []

        for c in S:
            if c.isalpha():
                S_list.append(characters.pop())
            else:
                S_list.append(c)
        return "".join(S_list)