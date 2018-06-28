n=int(input())
l=[]
for i in range(n):
	try:
		a=int(input())
		l.append(a)
		l[::-1]
		print(l)
	except:
		break
