class Solution:
    def containsDuplicate(self, nums,k):
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i-seen[nums[i]]<=k:
                    return True
            seen[nums[i]]=i
        return False
object = Solution()
print(object.containsDuplicate([1,2,3,4,5,6,7,8,9,10], 3))