def ordburbuja(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
            
def ordinsercion(arr):
    
    for actual in range(1,len(arr)):
        sig = actual
        while sig>0 and arr[sig -1]>arr[sig]:
            arr[sig],arr[sig-1]=arr[sig-1],arr[sig]
            sig = sig-1
            
            
a = [2,8,5,3,9,4,1]
ordburbuja(a)
print("Ordenamiento burbuja ", a)


b = [2, 8, 5, 3, 9, 4, 1]
ordinsercion(b)
print("Ordenamiento insercion ", b)