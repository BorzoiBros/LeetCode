class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i in s:
            num += roman_num[i]
        if "IV" in s or "IX" in s:
            num -= 2
        if "XL" in s or "XC" in s:
            num -= 20
        if "CD" in s or "CM" in s:
            num -= 200
        return num

solution = Solution()
print(solution.romanToInt(""))

        
