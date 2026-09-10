class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return  False 
        c = set(s) 
        for i in c : 
            if s.count(i) != t.count(i):
                return False 
        return True 
    