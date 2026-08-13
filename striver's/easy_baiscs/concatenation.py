class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(2):
            for x in nums:
                ans.append(x)
        return ans

obj = Solution()                    # Create an object
print(obj.getConcatenation([1, 2, 1]))