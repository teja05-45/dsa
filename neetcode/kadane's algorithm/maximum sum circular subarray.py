class Solution:
    def maxSubarraySumCircular(self, nums):
        
        total = sum(nums)
        currMax = maxSum = nums[0]
        currMin = minSum = nums[0]

        for num in nums[1:]:
            currMax = max(currMax + num, num)
            maxSum = max(maxSum, currMax)

            currMin = min(currMin + num, num)
            minSum = min(currMin, minSum)
        
        if maxSum < 0:
            return maxSum
        else:
            return max(maxSum, total - minSum)

object = Solution()
print(object.maxSubarraySumCircular([1,-2,3,-2]))  # Output: 3