class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        for id in set(s):
            if s.count(id)!=t.count(id):
                return False
        return True
    

#optimal solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1={}
        freq_2={}
        for ch in s.lower():
            ch.isalpha()
            if ch in freq_1:
                freq_1[ch]+=1
            else:
                freq_1[ch]=1
        for ch in t.lower():
            ch.isalpha()
            if ch in freq_2:
                freq_2[ch]+=1
            else:
                freq_2[ch]=1
            
        return freq_1 == freq_2

obj=Solution()
print(obj.isAnagram("listen", "silent"))  # Output: True