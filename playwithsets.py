myset = {"Monday","Tuesday","Thursday","Wednesday","Thursday"}

print(myset)
myset.add("Friday")
print(myset)
newset = {1,2,3}
newset.add(4)
print(newset)
updatedset = {1,2,3,4}
updatedset.update({1,3,4,5})
print(updatedset)
updatedset.remove(1)
print(updatedset)
updatedset.discard(1)
print(updatedset)


actual_set = {1,3,4,5,7,9}
expected_set= {2,4,6,8,0}

union_set = actual_set.union(expected_set)
print(union_set)

inter_set = actual_set.intersection(expected_set)
print(inter_set)

differ_set = actual_set.difference(expected_set)
print(differ_set)

# this one remover reudndant values :

sym_differ_set = actual_set.symmetric_difference(expected_set)
print(sym_differ_set)

if actual_set.issubset(expected_set):
    print("Yes")
else:
    print("No")

a_set = set (range(10))
print(a_set)
for x in a_set:
    y = x ** 2
    print("this is the value"+str(y))