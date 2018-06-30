k=int(input())
bc=[]
x=[]
for i in range(k):
	mn=int(input())
	bc.append(mn)
for j in range(k):
	if((j%2==0) and (bc[j]%2!=0)):
		x.append(c[j])
	elif((j%2!=0) and (bc[j]%2==0)):
		x.append(bc[j])
print(x)		
