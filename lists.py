l1=[1,65,90,46,90,0,90]

l1.append(15)

print(f"append = {l1}")

l1.sort()

print(f"sort = {l1}")

l1.sort(reverse=True)

print(f"sort in dcending = {l1}")

l1.insert(3,30)

print(f"insert = {l1}")

l1.pop(2)

print(f"pop = {l1}")

l1.remove(90)

print(f"remove = {l1}")

print(f"Length = {len(l1)}")

print(l1.index(46))