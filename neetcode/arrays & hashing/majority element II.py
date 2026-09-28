class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collection import Counter
        thresh=len(nums)//3
        counts=Counter(nums)
        return [num for num , count in counts.items() if count>thresh]
        