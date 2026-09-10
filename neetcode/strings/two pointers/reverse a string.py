class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left < right:
            if (s[left]!=s[right]):
              s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

        return "".join(s)


obj = Solution()
print(obj.reverseString(["h","e","l","l","o"]))  # Output: "olleh"