def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            
            if arr[j]>arr[min]:
                min=j
            arr[j],arr[min]=arr[min],arr[j]
    return arr

arr=[1,7,6,5,4,2,3]
print(bubble_sort(arr))