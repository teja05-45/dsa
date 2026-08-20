from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        freq=Counter(nums)
        return [x for x , count in freq.most_common(k)]

obj=Solution()
print(obj.topKFrequent([1,1,1,2,2,3], 2))