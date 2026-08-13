class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


obj = Solution()

nums1 = [1, 2, 3, 0, 0, 0]

obj.merge(nums1, 3, [2, 5, 6], 3)

print(nums1)