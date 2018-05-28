a=int(input())
y=0
for i in range(2,a//2+1):
    if(a%i==0):
        y=y+1
if(y<=0):
    print("yes")
else:
    print("no")
