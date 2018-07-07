p=int(input())
q=input().split()
v=q[0:p]
s=0
h=[]
try:
	for i in range(0,len(v)):
		s=s+int(v[i])
		if(s>0):
			u=s
			h.append(u)
	print(max(h))		
		
except:
	print("invalid data")
	
