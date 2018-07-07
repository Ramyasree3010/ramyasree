class stk:
    def __init__(full):
        full.items = []
 
    def is_empty(full):
        return full.items == []
 
    def push(full,data):
        full.items.append(data)
 
    def pop(full):
        return full.items.pop()
 
 
q= stk()
rad=input()
 
for character in rad:
    q.push(character)
 
reversed_rad = ''
while not q.is_empty():
    reversed_rad = reversed_rad + q.pop()
if rad == reversed_rad:
    print('YES')
else:
    print('NO')
