class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0 
        size = len(s)

        for i in range(size): 
            
            l, r = i, i

            while l >= 0 and r < size and s[l] == s[r]: 
                l -= 1 
                r += 1 
                count += 1

            l, r = i, i + 1

            while l >= 0 and r < size and s[l] == s[r]: 
                l -= 1 
                r += 1 
                count += 1 
        
        return count

obj=Solution()
print(obj.countSubstrings("abc"))  # Output: 3
