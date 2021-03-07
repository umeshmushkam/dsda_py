friends = ["raj", "sarbani", "selena", "kitty"]       #print a list for each iteration
for friend in friends:
    print(friend)

friends = ["raj", "sarbani", "selena", "kitty"]       #print a list end with space on each line
for friend in friends:
    print(friend, end=" ")
print()

for i in range(5):                 #print itration i from range 0 -4
    print(i)
for j in range(5):                  #tp remove 0 from the list add +1
    print("Iteration", j+1)

for a in range(50, 101):
    print(a, end=" ")
print()

for a in range(50, 101, 2):
    print(a, end=" ")
print()

for a in range(231, 501, 2):
    print(a, end=" ")
print()

for b in range(200, -1 , -1):
    print(b, end=" ")
print()

for c in range(10):
    print(c)
print(sum(range(10)))

sum = 0
for c in range(10):
    print(c)
    sum += c
print(sum)

for i in range(10):
    print(i, end=" ")
print(i)
my_list = list(range(10))
print(my_list)

foods = ["orange", "bannana", "apple", "grape", "kiwi"]

for food in foods:
    f = len(foods)
    print(f)
    print(food, end=" ")
print()
#print(len(foods))
for i in range(len(foods)):
    print(i, foods[i], end=" ")
print()

print("one", end=" ")
print("line")
