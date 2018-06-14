num=int(input())
g=input().split()
g=int(g)
g=[]
for f in range(num):
	n=int(input())
	g.append(n)
max=0
for i in g:
	if i > max:
		max=i
print(max)		
