class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if (n == 1):
            return "1"
        if (n == 2):
            return "11"

        num_str = "11"
        for i in range(3, n + 1):
            num_str += '$'
            l = len(num_str)


            count = 1
            tmp_str = ""

            for j in range(1, l):

                if (num_str[j] != num_str[j - 1]):
                    tmp_str += str(count + 0)
                    tmp_str += num_str[j-1]

                    count = 1
                else:
                    count += 1
            num_str = tmp_str
        return num_str

solution = Solution()
print(solution.countAndSay(5))

