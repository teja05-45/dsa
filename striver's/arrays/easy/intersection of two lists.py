arr1 = list(map(int, input("enter the string:").split()))
arr2 = list(map(int, input("enter the secong:").split()))

merged =list(set(arr1)&set(arr2))
print(merged)