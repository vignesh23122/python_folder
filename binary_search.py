def binarysearch(arr,l,h,a):
    if l<=h:
        mid=l+(h-l)//2
        if arr[mid]==x:
            return mid
        elif x>arr[mid]:
            return binarysearch(arr,mid+1,h,a)
        elif x<arr[mid]:
            return binarysearch(arr,l,mid-1,a)
        
# arr=list(map(int,input("Enter the array\n").split()))
arr=[1,32,11,10,43,55,44,23,65]
arr.sort()
x=int(input("element to search \n"))
l=0
h=len(arr)
print(arr)
print(binarysearch(arr,l,h,x))