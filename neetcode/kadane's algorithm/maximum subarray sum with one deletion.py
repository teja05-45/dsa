class Solution(object):
    def maximumSum(self, arr):
        max_sum = float('-inf')
        max_one_delete = float('-inf')
        result = float('-inf')

        for i, a in enumerate(arr):
            prev_no_delete = max_sum

            max_sum = max(a, max_sum + a)

            max_one_delete = max(
                prev_no_delete,
                max_one_delete + a
            )

            result = max(result, max_sum, max_one_delete)

        return result

obj = Solution()
print(obj.maximumSum([1,-2,0,3]))  # Output: 4