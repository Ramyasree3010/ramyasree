
nterms =[]
res=[]
for i in range(0,1):
	a=int(input())
	nterms.append(a)
n1 = 0
n2 = 1
count = 0
if nterms[0] <= 0:
   print("Please enter a positive integer")
elif nterms[0] == 1:
   print("Fibonacci sequence upto",nterms,":")
   res.append(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms[0]:
       res.append(n1)
       nth =n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print(res)  
