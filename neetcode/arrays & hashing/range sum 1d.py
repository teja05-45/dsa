class Solution:
    def __init__(self,nums):
        self.prefix=[0]
        for n in nums:
            self.prefix.append(self.prefix[-1]+n)

    def sumRange(self,left,right):
        return self.prefix[right+1]-self.prefix[left]

obj=Solution([-2,0,3,-5,2,-1])
print(obj.sumRange(0,2))