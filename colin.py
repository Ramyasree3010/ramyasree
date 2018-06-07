def collinear(a, b, c, d, e, f):
     
   
    v = a * (d-f) + c * (f-b) + e * (b-d)
 
    if (v == 0):
        print ("yes")
    else:
        print ("no")
 

a,b=input().split()
c,d=input().split()
e,f=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)

collinear(a,b,c,d,e,f)
