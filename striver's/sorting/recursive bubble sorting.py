def bubble_sort(arr, n):
    # Base Case
    if n == 1:
        return

    # One pass of Bubble Sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call
    bubble_sort(arr, n - 1)


arr = [5, 1, 4, 2, 8]

bubble_sort(arr, len(arr))
print(arr)