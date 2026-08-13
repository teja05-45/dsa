#using single pointer
'''def palindrome(s,i):
    n=len(s)
    if i>n//2:
        return True
    if s[i]!=s[n-1-i]:
        return False
    return palindrome(s,i+1)

s = input("Enter a string: ")
if palindrome(s,0):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")'''


def palindrome(l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return palindrome(l+1,r-1)

s = input("Enter a string: ")
if palindrome(0, len(s) - 1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")