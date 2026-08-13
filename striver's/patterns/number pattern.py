n=5
for i in range(n):
    for j in range(i):
        print(j+1,end=" ")
    for k in range(2*(n-i)-1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")
    print()

