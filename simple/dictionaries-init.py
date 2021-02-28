# first take on dictionaries

d = {'one':1, 'two': 2,'three':3}
d['four'] = 4 # add an item
d.update({'five': 5, 'six': 6})

print(d)

print('five' in d) 

# sorted

print(sorted(list(d)))
print(sorted(list(d.values())))

print(sorted(list(d.items())))

print(sorted(list(d), key = d.__getitem__))

print([value for (key,value) in sorted(d.items())])

print([key for (key,value) in sorted(d.items())])

print(sorted(list(d), key = d.__getitem__, reverse =True))

d2 ={'one':'uno' , 'two':'deux', 'three':'trois', 'four': 'quatre', 'five':
   'cinq', 'six':'six'}

print(sorted(d2, key=d.__getitem__))

print(sorted(d2, key=d.__getitem__))

print([d2[i] for i in sorted(d2, key=d.__getitem__)])