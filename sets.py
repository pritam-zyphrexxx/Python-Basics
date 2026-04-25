s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}

s.add(20)
print(f"add: \n{s}")

s.remove(3)  # remove raises an error if the element is not found
print(s)

s.discard(10)  # discard does not raise an error if the element is not found
print(s)

s.pop()  # removes and returns an arbitrary element from the set
print(s)

s.clear()  # removes all elements from the set
print(f"clear: \n{s}")


s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

s1={21,22,23,24,25,26,27,28,29,30,31,32,33}

print(f": \n\n{s.union(s1)}")  # union of two sets

print(f"intersection: \n{s.intersection(s1)}")  # intersection of two sets

print(f"difference: \n{s.difference(s1)}")  # difference of two sets

print(f"difference_update: \n{s.difference_update(s1)}")  # difference update of two sets

print(f"symmertric difference: \n{s.symmetric_difference(s1)}")  # symmetric difference of two sets

print(f"subset:\n{s.issubset(s1)}")  # checks if s is a subset of s1

print(f"superset: \n{s.issuperset(s1)}")  # checks if s is a superset of s1

print(f"disjoint: \n{s.isdisjoint(s1)}")  # checks if s and s1 have no elements in common

