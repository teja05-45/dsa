class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxsum = minsum = ans = 0

        for num in nums:
            maxsum = max(num, maxsum + num)
            minsum = min(num, minsum + num)
            ans = max(ans, maxsum, abs(minsum))

        return ans

obj=Solution()
print(obj.maxAbsoluteSum([1,-3,2, -5, 4]))  # Output: 8
