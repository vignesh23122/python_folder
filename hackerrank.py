#find the square and diff of n sqr numbers

# T=int(input())
# res=[]
# for i in range(T):
#     li=[]
#     n=int(input())
#     a=0
#     for j in range(1,n+1):
#         a+=(j**2)
#         li.append(j)
#     b=sum(li)
#     result=(b**2)-a
#     b=0
#     res.append(result)
# print(*res,sep="\n")

# NTH PRIME

# t=int(input())
# a=0

# for i in range(t):
#     n=int(input())
#     a+=n
# c=str(a)
# d=c[0:10]
# print(d)


#fibonanci

# t=int(input())
# a=1
# b=2
# li=[]
# l2=[]
# for i in range(t):
#     n=int(input())
#     for j in range(n):
#         if a<=n:
#             if a%2==0:
#                 li.append(a)
            
#             a+=b
#             a,b=b,a
#     l2.append(sum(li))
# print(*l2,sep="\n")

#LCM OF N NUMBERS

# def __gcd(a, b):
# 	if (a == 0):
# 		return b
# 	return __gcd(b % a, a)

# def LcmOfArray(arr, idx):
# 	if (idx == len(arr)-1):
# 		return arr[idx]
# 	a = arr[idx]
# 	b = LcmOfArray(arr, idx+1)
# 	return int(a*b/__gcd(a,b))

# n=int(input())
# li=[]
# for i in range(n):
#     arr=[x for x in range(1,int(input())+1)]
#     li.append(LcmOfArray(arr,0))
# print(*li,sep="\n")
    

#SUMMATION OF PRIME

# n=int(input())
# for i in range(n):
# 	t=int(input())
# 	for j in range(t):
		
# n=int(input())
# for k in range(n):
# 	n=int(input())
# 	dt={}
# 	prime=2
# 	count=0
# 	for i in range(2,n+1):
# 		for j in range(2,i):
# 			if prime%j==0:
# 				count+=1
# 			else:
# 				continue
	
# 		dt[prime]=count
# 		count=0	
# 		prime+=1
# 	li=list(dt.values())[0]
# 	res=[]
# 	for i in dt:
# 		if dt[i]==li:
# 			res.append(i)
# 	print(sum(res))


