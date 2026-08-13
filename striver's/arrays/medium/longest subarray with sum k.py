class Solution:
    def longestSubarray(self, nums, k):
        prefix = 0
        longest = 0
        prefix_map = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - k in prefix_map:
                longest = max(longest, i - prefix_map[prefix - k])

            if prefix not in prefix_map:
                prefix_map[prefix] = i

        return longest
    

nums=[1, 2, 3, 4, 5]
k=3
obj=Solution()
print(obj.longestSubarray(nums,k))                  