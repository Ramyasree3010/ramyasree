def repeat(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				return l[i]
	print(l[i])
def main():
	n=int(raw_input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	repeat(l)
try:
	main()
except:
	print('invalid')
