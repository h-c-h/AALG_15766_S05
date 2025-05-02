def ordinsercion(arr):
    
    for actual in range(1,len(arr)):
        sig = actual
        while sig>0 and arr[sig -1]>arr[sig]:
            arr[sig],arr[sig-1]=arr[sig-1],arr[sig]
            sig = sig-1
            
            
a = [2,8,5,3,9,4,1]
ordinsercion(a)
print(a)
            