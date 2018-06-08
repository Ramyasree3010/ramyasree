s=str(input())
r=list(s)
g=''
for i in range(0,len(s)-1,2):
	t=r[i]
	r[i]=r[i+1]
	r[i+1]=t
	g=g+r[i]+r[i+1]
if (len(r)%2!=0):
	g=g+r[i+2]
print(g)	
