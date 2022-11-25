from operator import index, indexOf


def res(jac,jil,j,l):
    if len(jac)!=0:
        j+=max(jac)
        k=index(max(jac))
        jac.remove(k)
        jil.remove(k)


        



n=int(input())
jac=list(map(int,input().split()))[:n]
jil=list(map(int,input().split()))[:n]
j,l=0,0
result=res(jac,jil,j,l)
print(result)
