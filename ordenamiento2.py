def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

a = [2, 8, 5, 3, 9, 4, 1]
bubble_sort(a)
print(a)