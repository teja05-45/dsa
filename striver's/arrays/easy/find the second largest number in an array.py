arr=[1,2,1,3,5,67,7,5,43,2]
largest=arr[0]
second_largest=float('-inf')
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    else:
        if num>second_largest and num!=largest:
            second_largest=num
            
print(second_largest)