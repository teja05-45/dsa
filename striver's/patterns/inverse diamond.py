n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print(k+1,end=" ")
    print()



for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print(i+1,end=" ")
    print()