class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
            
        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
            
        result = []
        if p_count == s_count:
            result.append(0)

        left = 0
        for right in range(len(p), len(s)):
            s_count[ord(s[right]) - ord('a')] += 1
            s_count[ord(s[left]) - ord('a')] -= 1
            
            left += 1

            if s_count == p_count:
                result.append(left)
                
        return result