def longestSubarray(nums, k):
    prefix_sum = 0
    first_occurrence = {}
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        # Subarray starts from index 0
        if prefix_sum == k:
            max_len = i + 1

        # Check if a previous prefix makes sum = k
        if (prefix_sum - k) in first_occurrence:
            max_len = max(max_len, i - first_occurrence[prefix_sum - k])

        # Store first occurrence only
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i

    return max_len

nums = [2, -1, 2, 3, -2, 1]
k = 4
print(longestSubarray(nums, k))   # 5