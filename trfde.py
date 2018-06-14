l,u=input().split()
l = int(l) 
u = int(u)

for num in range(l,u):

   
   order = len(str(num))
    
   
   sum = 0

   
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num,end=" ")
