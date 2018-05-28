g=int(input())
sum = 0
x = g
while x > 0:
   p= x % 10
   sum += p ** 3
   x//= 10
if g == sum:
   print("yes")
else:
   print("no")
