def insertion_sort(arr, n):
    # Base Case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertion_sort(arr, n - 1)

    # Insert last element at its correct position
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


arr = [12, 11, 13, 5, 6]

insertion_sort(arr, len(arr))
print(arr)