def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1,num2=input().split()
num1=int(num1)
num2=int(num2)

print(computeHCF(num1, num2))