def first(y,z):
    count=0
    if len(y)<len(z):
        w=len(y)
    else:
        w=len(z)
    for a in range(0,w):
        if y[a]==z[a]:
            count+=1
        else:
            break
    return y[:count]
pre=input()
q=[]
for x in range(0,pre):
    q.append(raw_input())
for x in range(0,pre-1):
    
    q[x+1]=first(q[x],q[x+1])
print q.pop()
