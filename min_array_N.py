num=int(input())
g=input().split()
min=999999
for i in g:
	if int (i) <int(min):
		min=i
print(int(min))
