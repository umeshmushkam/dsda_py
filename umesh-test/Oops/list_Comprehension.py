healthy = ["Kale chips", "broccoli", "salad"]
backpack = ["burger","fries","Kale chips","salad","onion rings"]

# healthy_backpack = [hfood for hfood in backpack if hfood in healthy]
# print(healthy_backpack)

healthyfood = []
for item in backpack:
    if item in healthy:
        healthyfood.append(item.upper())
print(healthyfood)



cube = []
for number in range(10):
    cube.append(number ** 3)
print(cube)

cubes = [num**3 for num in range(10)]
print(cubes)

cubes = [num**3 for num in range(10) if num % 2 == 0]
print(cubes)

cubes = [num**3 for num in range(10) if num % 2 == 1]
print(cubes)