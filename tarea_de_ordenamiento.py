def ordburbuja(arr):
     for pas in range(1, len(arr)):
        for actual in range(0, len(arr) - pas):
            if arr[actual] > arr[actual + 1]:
                arr[actual], arr[actual + 1] = arr[actual + 1], arr[actual]
                
            
def ordinsercion(arr):
    
    for actual in range(1,len(arr)):
        sig = actual
        while sig>0 and arr[sig -1]>arr[sig]:
            arr[sig],arr[sig-1]=arr[sig-1],arr[sig]
            sig = sig-1
            
            
a = [2,8,5,3,9,4,1]
ordburbuja(a)
print("Ordenamiento burbuja ", a)


b = [2,8,5,3,9,4,1]
ordinsercion(b)
print("Ordenamiento insercion ", b)