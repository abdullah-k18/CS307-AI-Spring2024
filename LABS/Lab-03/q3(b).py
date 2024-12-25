X = {1, 2, 3, 4, 5, 6}
Y = {2, 4, 6, 8}
#UNION
union = X.union(Y)
print("X u Y = ", union)
#INTERSECTION
intersection = X.intersection(Y)
print("X n Y =", intersection)
#DIFFERENCE
difference = X.difference(Y)
print("X - Y = ", difference)
#ADDING AN ELEMENT
Z = {1, 2, 3, 4}
print("Z =", Z)
Z.add(5)
print("After Adding a New Element, Z = ", Z)
#REMOVING AN ELEMENT
print("Z = ", Z)
Z.remove(4)
print("After Removing an Element, Z =", Z)
#CLEARING A SET
print("Z =", Z)
Z.clear()
print("After Clearing, Z =", Z)