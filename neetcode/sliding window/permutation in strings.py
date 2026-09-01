from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq=Counter(s1)
        curr={}
        left=0
        for right in range(len(s2)):
            curr[s2[right]]=curr.get(s2[right],0)+1
            if (right-left+1)>len(s1):
               curr[s2[left]]-=1
               if  curr[s2[left]]==0:
                 del curr[s2[left]]
               left+=1

            if curr==s1_freq:
                return True
        return False