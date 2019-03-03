# https://leetcode.com/problems/shortest-distance-to-a-character/

S = "loveleetcode"
C = "e"

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance_to_char_list = []
        indices_character = []
        for i in range(len(S)):
        	if S[i] == C:
        		indices_character.append(i)
        print("Indices of", C, indices_character)
        for j in range(len(S)):
        	shortest_distance_to_char = abs(j - indices_character[0])
        	print("Shortest distance of", S[j], "is", shortest_distance_to_char)
        	for l in indices_character[1:]:
        		if shortest_distance_to_char > abs(j - l):
        			shortest_distance_to_char = abs(j - l)
        	distance_to_char_list.append(shortest_distance_to_char)

        return distance_to_char_list


solution = Solution()
print(solution.shortestToChar(S,C))