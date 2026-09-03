class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int


        [2,3,-2,4]
        2 
        2 * 3 = 6
        2 * 3 * -2 = -12
        2 * 3 * -2 * -4 = 48
        """

        largest = nums[0]
        smallest = nums[0]
        result = nums[0]
        for i in nums[1:]:
            possible = (i, smallest * i, largest * i)
            largest = max(possible)
            smallest = min(possible)
            result = max(result, largest)
        
        return result

object = Solution()
print(object.maxProduct([2,3,-2,4]))  # Output: 6


#if i want to return the subarray as well, we can do the following:
class Solution2():
    def maxProductSubarray2(self, nums):
        largest = nums[0]
        smallest = nums[0]
        result = nums[0]

        largest_start = 0
        smallest_start = 0

        best_start = 0
        best_end = 0

        for i in range(1, len(nums)):
            num = nums[i]

            # Three possible products
            candidates = [
                (num, i),
                (largest * num, largest_start),
                (smallest * num, smallest_start)
            ]

            # Find largest and smallest product
            largest, largest_start = max(candidates)
            smallest, smallest_start = min(candidates)

            # Update best result
            if largest > result:
                result = largest
                best_start = largest_start
                best_end = i

        return nums[best_start:best_end + 1]

obj = Solution2()
print(obj.maxProductSubarray2([2,3,-2,4]))  # Output: [2, 3]