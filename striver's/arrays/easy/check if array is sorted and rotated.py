class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        count=1
        if n==1:
            return True
        for i in range(2*n):
            if nums[(i-1)%n]<nums[i%n]:
                count+=1
            else:
                count=1
            if count==n:
             return True
        return False        