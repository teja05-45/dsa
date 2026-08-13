#optimal
class Solution:
    def getConcatenation(self, nums):
        return nums + nums

obj = Solution()
print(obj.getConcatenation([1, 2, 3]))  # Output: [1, 2, 3, 1, 2, 3]

#brute force
class Solution:
    def getConcatenation(self, nums):
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result

obj = Solution()
print(obj.getConcatenation([1, 2, 3]))  # Output: [1, 2, 3, 1, 2, 3]