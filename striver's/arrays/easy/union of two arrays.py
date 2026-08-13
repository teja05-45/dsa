class Solution:
    def unionArray(self, nums1, nums2):
        num3=nums1+nums2
        num3.sort()
        return list(dict.fromkeys(num3))