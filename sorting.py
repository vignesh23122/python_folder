def sorting(arr):
    temp=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i]<arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp

            else:
                pass
    return arr
arr=[10,9,19,34,23]
print(sorting(arr))