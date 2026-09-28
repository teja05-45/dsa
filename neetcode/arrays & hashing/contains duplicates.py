#brute force approach
class Solution:
    def hasDuplicate(self, nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False    

obj = Solution()
print(obj.hasDuplicate([1, 2, 3, 4, 5]))  # Output: False    

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

#optimal approach
class Solution:
    def hasDuplicate(self, nums):
        return len(nums) != len(set(nums))

obj = Solution()
print(obj.hasDuplicate([1, 2, 3, 4, 5,5,5]))  # Output: True