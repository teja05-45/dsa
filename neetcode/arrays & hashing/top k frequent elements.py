from collections import Counter
class Solution():
    def topK(self,nums,k):
        counts=Counter(nums)
        return [num for num , count in counts.most_common(k)]