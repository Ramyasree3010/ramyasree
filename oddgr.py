lower,upper=input().split()
lower=int(lower)
upper=int(upper)
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i,end=" ")
