class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l=0
        r=len(nums)-1
        i=0
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]

        while i<=r:
            if nums[i]==0:
                swap(i,l)
                l+=1
            
            elif nums[i]==2:
                swap(i,r)
                r-=1
                i-=1
            i+=1
        return nums

obj = Solution()
print(obj.sortColors([2, 0, 2, 1, 1, 0]))