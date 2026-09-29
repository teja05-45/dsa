class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen={}
      for i,num in enumerate(nums):
        diff=target-num
        if diff in seen:
           return [seen[diff]+1,i+1]
        seen[num]=i
      return nums
      

          
