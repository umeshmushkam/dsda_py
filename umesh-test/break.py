"""
languages = ["c++", "java", "python", "Jscripts"]
print("What are you searching for?")                    #break
lang = input()

for language in languages:
    print(language)
    if language == lang: #checks for the input data and prints the input given
        print("We found the lang" + lang)
        break
    print("end of the iteration") #input doesn't macth prints the "end"

"""
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:                   #continue
    print(language)
    if language == lang:
        print("we found the lang " + lang)
        continue
    print(language + " ...Not what we are looking for...")

""" 
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:                  #if else
    if language == lang:
        print("we found the lang " + lang)
    else:
        print(language + " ...Not what we are looking for...")

"""
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:                  # prints only the input values
    if language == lang:
        print("we found the lang " + lang)
"""
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:                  # passes the code without error
    if language == lang:
        pass
  """  
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:                  # passes the code without error
    if language == lang:
        print(language + "was found.")
print("Loop is done")

"""
"""
languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()
for language in languages:              # when loop is break it will print the loop condition else print not found
    if language == lang:
        print(language + " was found.")
        break
else:
     print("Not Found")

"""

"""

languages = ["c++", "java", "python", "Jscripts","Kia","python","java","python","jsapython","python"]
print("What are you searching for?")
lang = input()

found = False

for language in languages:              # when loop is break it will print the loop condition else print not found
    if language == lang:
        print(language + " was found.")
        found = True
if not found:

     print("Not Found")

"""
"""

i = 5                                       #initialization
while i < 20:                               #Condition
    print(i)                        
    i += 5                                  #update              


for i in range(0 , 10 , 5):
    print(i)
"""

"""
numbers = [5, 6, 40, 7, 55, 60, 70, 8, 9]

j = 0
square = 500
while j < len(numbers):
    if numbers[j] ** 2 > square:
        print(numbers[j], "squared is larger than", square)
        break
    j += 1 
"""
"""
numbers = [5, 6, 4, 7, 5, 6, 7, 8, 90]

j = 0
square = 500
while j < len(numbers):
    if numbers[j] ** 2 > square:
        print(numbers[j], "squared is larger than", square)
        break
    else:
        print(numbers[j], "squared are not larger then", square)
    j += 1 

"""
"""
numbers = [5, 6, 4, 7, 5, 6, 7, 8, 90]

j = 0
square = 500
while j < len(numbers):
    if numbers[j] ** 2 > square:
        print(numbers[j], "squared is larger than", square)
        break
    print(numbers[j], "squared are not larger then", square)
    j += 1 
else:
    print("None squared is lareger than", square)

"""
"""
numbers = [2, 5, 8, 4, 10, 9, 7, 6]
i=0
square = 500
sucess = False

while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "Squyared is larger number", square)
        sucess = True
        break
    print(numbers[i], "Squared is not larger than", square)
    i += 1
if sucess:
    print("One of them is large enough!!")
if not sucess:
    print("none were large enough")

"""
"""
print("Doy ou waant to continue ? Please press Y/N")
resposne = input()
while resposne == "Y":
    print("Do you want to continue")
    response = input()

"""
"""
while True:
    print("Q to quit")
    resposne = input()
    if resposne == "Q":
        break

"""
"""
while True:
    print("Countinue ? Y?N")
    response = input()
    if response != "y" and response != "Y":
        break

"""
"""
while True:
    print("Continue ? Press Y?N")
    response = input()
    if response.lower() != "y":
        break


"""
"""
while True:
    print("Continue ? Y/N")
    response = input()
    if response.isupper():
        print("It's upper case")
    if response.lower() != "y":
        break

"""
"""
logging = False
logging_in = True
name = "umesh"
if logging_in:
    if logging:
        print(name + " is logging in")
    print("Welcome ", name)


x = input("Enter your name ")
print("Hello," + x)

"""
"""
#Age = input("Please enter your age ?")
#fun = int(fun)
Age = 40
fun = False
like_to_dance = True

if (Age < 30 or fun) and like_to_dance:
    print("You are invited !!")
else:
    print("Get away you old scum")

Age = input("Please enter your age ?")
fun = False
like_to_dance = True

if Age < 30:
    if fun:
        if like_to_dance:
            print("you are invited....")
        else:
            print("Get away you old scum") """







































