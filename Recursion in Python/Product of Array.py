def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])

arr=[1,2,3]
print(productOfArray(arr))
