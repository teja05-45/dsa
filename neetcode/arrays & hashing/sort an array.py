class Solution(object):
    def sortArray(self, nums):
        MIN=min(nums)
        MAX= max(nums)
        count =[0]*(MAX-MIN + 1)
        for x in nums:
            count[x - MIN] += 1
        result = []
        for i in range(len(count)):
            result += [i + MIN] * count[i]
        return result