class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        
obj = Solution()

print(obj.isPalindrome("madam"))    # True
print(obj.isPalindrome("hello"))    # False
print(obj.isPalindrome("racecar"))  # True      