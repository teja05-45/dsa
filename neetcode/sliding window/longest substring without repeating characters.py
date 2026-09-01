class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        empty=set()
        left=0
        max_length=0
        for right in range (len(s)):
            while s[right] in empty:
                empty.remove(s[left])
                left+=1
            empty.add(s[right])

            window=right-left+1
            if window>max_length:
                max_length=window
        return max_length

object = Solution()
print(object.lengthOfLongestSubstring("abcabcbb"))