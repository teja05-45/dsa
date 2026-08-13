arr=[1,1,3,42,4,2,1,2]
result=[]
for num in arr:
    if arr.count(num) > 1 and num not in result:
        result.append(num)

print(result)


