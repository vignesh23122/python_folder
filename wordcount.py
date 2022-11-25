from posixpath import split


def wordcount(li):
    l2=[]
    c=0
    digit=[]
    
    if len(li)>=2:
        for i in range(0,len(li)):
            b=len(li[i])
            l2.append(b)
        for j in range(0,len(l2)):
            c+=l2[j]

    return c,splittingnumbers(c)

def splittingnumbers(c):
    d=0
    for k in str(c):
        d=d+int(k)
    # if d==10:
    #     splittingnumbers(d)
    return d

li=list(map(str,input().split()))
print(wordcount(li))