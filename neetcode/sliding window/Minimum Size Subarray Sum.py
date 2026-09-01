class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)

                window_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length
obj=Solution()
print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))