class Solution:
    def twosum(self,nums,target):
        num_dict={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in num_dict:
                return [num_dict[complement]+1,i+1]
            num_dict[num]=i

obj=Solution()
print(obj.twosum([2, 7, 11, 15, -2 ], 5))