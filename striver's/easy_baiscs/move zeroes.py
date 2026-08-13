def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

# Example usage:
nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))