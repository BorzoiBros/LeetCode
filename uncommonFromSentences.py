class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        word_A = A.split()
        word_B = B.split()
        common = []
        uncommon_tmp = []
        uncommon = []
        for A in word_A:
            for B in word_B:
                if A == B:
                   common.append(B)
        for A in word_A:
            if A not in common:
                uncommon_tmp.append(A)
        for B in word_B:
            if B not in common:
                uncommon_tmp.append(B)
        for i in uncommon_tmp:
            if uncommon_tmp.count(i)  == 1:
                uncommon.append(i)
        return uncommon

A = "apple apple"
B = "banana"

solution = Solution()
print(solution.uncommonFromSentences(A,B))
