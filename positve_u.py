p=int(input())
q=0
while True:
	try:
		w=input().split()
		z=len(w)
		for i in range(0,z):
			q=q+int(w[i])
	except:
		break
print (q,end=" ")
