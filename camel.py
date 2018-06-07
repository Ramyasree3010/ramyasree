a=input()
b=a.split()
c=len(b)
e=c
d=[]
i=0
j=0
while c>0:
    d=list(b[i])
    e=d[0].upper()
    h=len(d)
    h=h-1
    d[0]=e
    k=1
    while h>0:
        d[k]=d[k].lower()
        k=k+1
        h=h-1
    print("".join(d)," ",end="")
    i=i+1
    c=c-1
