class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            x=nums[i]*nums[i]
            ans.append(x)
        ans.sort()

        return ans
    
obj=Solution()
print(obj.sortedSquares([-4,-3,0,9,7]))        