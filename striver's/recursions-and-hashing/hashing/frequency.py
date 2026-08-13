arr = [1, 2, 1, 3, 1, 3, 4, 2]
n = 1

def f(n, arr):
    count = 0

    for i in arr:
        if i == n:
            count += 1

    return count

print(f(n, arr))



arr = [1, 2, 1, 3, 1, 3, 4, 2]

hash_arr = [0] * 13   # indices 0 to 12

for num in arr:
    hash_arr[num] += 1

print(hash_arr[1])   # 3
print(hash_arr[2])   # 2
print(hash_arr[3])   # 2
print(hash_arr[4])   # 1



#using hashing
arr=[1,2,1,3,2,4,5,6,7]
hashmap={}
for num in arr:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1

n=int(input("Enter a number: "))
if n in hashmap:
    print("frequency of n is :",hashmap[n])
else:
    print("frequency is not there")
