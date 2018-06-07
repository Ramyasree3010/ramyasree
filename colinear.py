def collinear(x1, y1, x2, y2, x3, y3):
     
   
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
 
    if (a == 0):
        print ("Yes")
    else:
        print ("No")
 

x1,y1=input().split()
x2,y2=input().split()
x3,y3=input().split()
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
x3=int(x3)
y3=int(y3)

collinear(x1, y1, x2, y2, x3, y3)
