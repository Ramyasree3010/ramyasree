s,t,r=input().split()
if((s>=t)and(s>=r)):
	Largest=s
elif((t>=s)and(t>=r)):
	Largest=t
else:	
	Largest=r
print(Largest)
