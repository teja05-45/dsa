## iterative
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of",n,"is",fact)

#recursive
def recursive(n):
    n=int(input("enter the number:"))
    if n==0 or n==1:
        return 1
    return n*recursive(n-1)

n=int(input("enter the number:"))
print("factorial of",n,"is",recursive(n))
