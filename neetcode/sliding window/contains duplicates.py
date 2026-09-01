class Solution(object):
    def containsDuplicate(self, nums):
        empty = set()

        for i in range(len(nums)):
            if nums[i] in empty:
                return True
            empty.add(nums[i])

        return False
object = Solution()
print(object.containsDuplicate([1,2,3,4,5,6,7,8,9,10]))
