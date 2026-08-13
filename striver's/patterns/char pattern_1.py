n=5
for i in range(n):
    ch=ord('A')
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()
print("\n")

ch=ord('A')
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()
print("\n")


print("\n")
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()

print("\n")
n=5
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()


print("\n")
n = 5

for i in range(n):
    ch = ord('A') + i
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\n")

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    
    for j in range(i-1,-1,-1):
        print(chr(65+j),end=" ")

    print()

print("\n")

n = 5

for i in range(n):
    ch = ord('A') + i
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\n")


n=5
for i in range(5):
    ch=ord('A')+n-i-1   
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()