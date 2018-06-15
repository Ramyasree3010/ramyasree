num=int(input())
g=input().split()
max=0
for i in g:
	if int(i) >int(max):
		max=i
print(int(max))
