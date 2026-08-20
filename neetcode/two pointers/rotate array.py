class Solution:
    def rotate(self, nums, k):
        if nums:
            k=k%len(nums)
            nums[:]=nums[-k:]+nums[:-k]

obj=Solution()
nums = [1,2,3,4,5,6,7]

obj.rotate(nums, 3)

print(nums)