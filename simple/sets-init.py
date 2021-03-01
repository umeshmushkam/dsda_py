s1 = {'ab',3,4,(5,6)}
print(s1)

s2 = {'ab',7,(7,6)}
print(s2)

s3 = {'ab','ab',2,2} # unique values only
print(s3)

s3.add('xyz')
print(s3)

s4 = frozenset({'ab','=df',2,5})
print(s4)

s1.add(frozenset(s4)) # errors out 'frozenset' object has no attribute 'add'

print(s1-s2)
print(s1.intersection(s2))
print(s1.union(s2))

for element in s1 :print(element)

s1.clear()
print(s1)