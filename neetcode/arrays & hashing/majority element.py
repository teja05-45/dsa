class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

obj=Solution()
print(obj.majorityElement([3,2,3]))  # Output: 3