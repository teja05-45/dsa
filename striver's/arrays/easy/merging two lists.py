arr1 = list(map(int, input("Enter first list of numbers: ").split()))
arr2 = list(map(int, input("Enter second list of numbers: ").split()))

# Concatenates both lists
merged = arr1 + arr2

merged.sort()
print("Merged list:", merged)