class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_1 = {}
        freq_2 = {}
        
        
        for ch in s.lower():
            if ch.isalpha():
                if ch in freq_1:
                    freq_1[ch] += 1
                else:
                    freq_1[ch] = 1
    
        
        for ch in t.lower():
            if ch.isalpha():
                if ch in freq_2:
                    freq_2[ch] += 1
                else:
                    freq_2[ch] = 1
            
        
        return freq_1 == freq_2
