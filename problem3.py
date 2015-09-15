prims = []

for x in range(2, 600851475143):
    if x % 2 == 0:
        continue
    found = True
    for y in range(2, x-1):
        if x % y == 0:
            found = False
            break
    if found:
        print "Found prim", x
