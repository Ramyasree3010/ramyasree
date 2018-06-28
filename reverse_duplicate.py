f=input()
v=''.join([j for i,j in enumerate(f) if j not in f[:i]])
print(v)
