lower,upper = input().split()
lower=int(lower)
upper = int(upper)


for num in range(lower+1,upper):

   if num > 2:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
