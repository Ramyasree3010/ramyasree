r=int(input())
s=int(input())
t=int(input())
if((r>=s)and(r>=t)):
	Largest=r
elif((s>=r)and(s>=t)):
	Largest=s
else:	
	Largest=t
print(Largest)