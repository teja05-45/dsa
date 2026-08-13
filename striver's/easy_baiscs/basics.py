n=[3,5,2,8]
for i in n:
    print("numbers:",i)
    
for i in range(len(n)):
    print("len:",i)
    
print("sum:",sum(n))

print("max:",max(n))

print("min",min(n))

print("average:",sum(n)/len(n))

for i in n:
    if i%2==0:
        print("even:",i)
        
for i in n:
    if i%2!=0:
        print("odd:",i)

positive_count=0
for i in n:
    if i>0:
        positive_count+=1
print("positive",positive_count)

negative_count=0
for i in n:
    if i<0:
        negative+=1
print("negative:",negative_count)

un=list(set(n))
un.sort()
print("second:",un[-2])