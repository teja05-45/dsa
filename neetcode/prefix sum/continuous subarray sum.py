class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        p_sum = 0
        d = {0: -1}

        for index, num in enumerate(nums):
            p_sum += num
            target = p_sum % k

            if target in d:
                if index - d[target] >= 2:
                    return True
            else:
                d[target] = index

        return False