arr=['a','b','d','a','c','a','b','c','c']
hashmap={}

for i in arr:
    if i in hashmap:
        hashmap[i]+=1
    else:
        hashmap[i]=1

n=input("enter the string:")
if n in hashmap:
    print("frequency of n is :",hashmap[n])
else:
    print("not")