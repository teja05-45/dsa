class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        max_count=0
        left=0
        zeros=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1 
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            max_count=max(max_count,right-left+1)
        return max_count
            
        