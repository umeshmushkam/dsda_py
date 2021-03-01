from collections import Counter

c1 = Counter('anysequence')
print(c1)
c2 = Counter({'a': 1, 'c': 3,'e':5})
print(c2)
c3 = Counter(a=2,c=3,e=4)
print(c3)

ct = Counter()
print(ct)
ct.update('abcdd')
print(ct)
ct.update({'a': 3})
print(ct)

for item in ct:
    print('%s : %d' % (item, ct[item]))

print(c1.most_common())