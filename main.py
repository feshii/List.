l1 = [12,24,36,48,60,72,84,96,108,120]
print("list l1: ",l1)
l2 = [11,22,33,44,55,66,77,88,99,110]
print("list l2: ",l2)   
l1.extend(l2)
print("list l1 after extending: ",l1)
l1.sort()
print("list l1 after sorting: ",l1)