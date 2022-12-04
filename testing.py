# # a=int(input())
# # b=list(map(int,input().split()))[:a]
# # c=[]
# # c+=b[0:len(b)//2]
# # c+=c[::-1]
# # print(c)

# a = int(input())
# b=list(map(str,input("enter the desired special characters").split()))
# for i in range(1, a):
#     for j in range(i, a):
#         if j==i or i==1:
#             print(b[0], end=" ")
#         else:
#             print(" ",end=" ")
#     if i != a-1:
#         for k in range(0, i):
#             if k == 0 or k == (i-1):
#                 print(b[1], end=" ")
#             else:
#                 print(" ", end=" ")
#     else:
#         for k in range(0,i):
#             print(b[1],end=" ")
#     print()



# n=input()

# alpha=['a','e','i','o','u']
# dt={}
# for i in n:
#     if i in alpha:
#         c=n.count(i)
#         dt[i]=c
#     else:
#         pass
# maxx=max(zip(dt.values(),dt.keys()))[1]

# print(maxx)
# print(len(n))
# print(n)

        
# n=list(map(int,input().split()))
# a=len(n)
# ord=[]
# for i in n:
#     while i!=0:
#         r=i%10
#         i//=10
#         ord.append(r)
# ord.sort()
# print(a,'\n',ord)

# n=[2,3,5,8,0,6]
# k=8
# li=[]
# sar=[]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]-n[j]==k:
#             sar.append(n[i])
#             sar.append(n[j])
#             li.append(sar)
#             sar=[]
#         else:
#             pass
# if len(li)!=0:
#     print(li)
# else:
#     print("Null")


# for i in range(1,int(input())):
#     print(i%5==0,end="\n")



