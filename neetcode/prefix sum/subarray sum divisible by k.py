class Solution:
    def subarraysDivByK(self, nums, k):
        count = [0] * k
        count[0] = 1

        prefix = 0
        ans = 0

        for x in nums:
            prefix = (prefix + x) % k
            ans += count[prefix]
            count[prefix] += 1

        return ans