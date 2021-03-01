from collections import deque
import itertools

dq = deque('abc')
print(dq)

dq.append('d')
print(dq)

dq.appendleft('z')
print(dq)

dq.extend('efg')
print(dq)

print(dq.pop())
print(dq)
print(dq.popleft())
print(dq)

dq.rotate(2)
print(dq)

print(list(itertools.islice(dq,3,6)))

dq2=deque([],maxlen=3)
for i in range(6):
    dq2.append(i)
    print(dq2)