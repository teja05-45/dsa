class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            count = right - left + 1
            max_count = max(max_count, count)

        return max_count
obj=Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1]))  # Output: 4