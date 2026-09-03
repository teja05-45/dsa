class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum  = -999999
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
object = Solution()
print(object.maxSubArray([-2,1,-3,4,-1,2,1, -5, 4]))  # Output: 6

##if we want to return the subarray as well, we can do the following:
class Solution2():
    def maxSubArrayindex(self, nums):

        cur_sum = 0
        max_sum = float('-inf')

        start = 0
        best_start = 0
        best_end = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
                best_start = start
                best_end = i

            if cur_sum < 0:
                cur_sum = 0
                start = i + 1

        return nums[best_start:best_end + 1]


obj = Solution2()
print(obj.maxSubArrayindex([-2,1,-3,4,-1,2,1, -5, 4]))  # Output: [4, -1, 2, 1]   