class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub=nums[0]
        curr_sub=0
        for n in nums:
            if curr_sub<0:
                curr_sub=0
            curr_sub+=n
            max_sub=max(max_sub,curr_sub)
        return max_sub
    
nums=[-2,1,-3,4,-1,2,1,-5,4]
obj=Solution()
print(obj.maxSubArray(nums))
