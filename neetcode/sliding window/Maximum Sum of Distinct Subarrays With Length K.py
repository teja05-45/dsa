class Solution:
    def maximumSubarraySum(self, nums, k):
        left = 0
        curr_sum = 0
        max_sum = 0
        seen = set()

        for right in range(len(nums)):

            # If duplicate is found
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add current element
            seen.add(nums[right])
            curr_sum += nums[right]

            # Window size becomes k
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

                # Remove left element
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum