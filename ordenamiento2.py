def ordburbuja(arr):
    for pas in range(1, len(arr)):
        for actual in range(0, len(arr) - pas):
            if arr[actual] > arr[actual + 1]:
                arr[actual], arr[actual + 1] = arr[actual + 1], arr[actual]

a = [2, 8, 5, 3, 9, 4, 1]
ordburbuja(a)
print(a)