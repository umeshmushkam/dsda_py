print("Hi",5,"I know i am the new","0.7","Hello World")    #,end=" "

import math

result = 1000/3       #/ gives the boolean value
result1 = 100//3      #// gives the interger value
print(result1)

new_result = math.floor(result)     #gives lessen value
print(new_result)                   
new_result_1 = math.ceil(result)     #gives the higer value
print(new_result_1)

pizza = 1565123452214
people = 8
print("highest number is", pizza % people)

print(200 ** 2 )

a = 5
b = 10
print (a ** b)

import math
result = math.pow(3,5)
new_version = math.floor(result)
new_version1 = math.ceil(result)
print(new_version)
print(new_version1)
print(round(20/3), 0)
print((20/3 , 5))
import math
x = math.ceil(20/3)
x_1 = math.floor(20/3)
y = 5
print((x) , (y))
print(x_1 , y)
print(100 % 5)
Note = "Hello World \nHey How are you"
Note = "Hello World\tHey How are you"
print(Note)
msg = "\x41"
print(msg)
msg1 = "\""
print(msg1)
msg2 = "\\,"
print(msg2)
text = "Hey you're pretty"  #use "" if you use single quote in the string or vice versa
print(text)
test_1 = 'She said "thank you"'
print(test_1)
text2 = 'Hey you\'re pretty'  ##use back \ if you are using single quote wthin in the sing quote
print(text2)
full = text + " & " + test_1
print(full)
poem = ("This is all combined"    #everthing thing is in one line
"as one happy string... "
"what was the sound"
"it was the door bell"
"When i see you, my heart sing")
print(poem)                           #using """ we can divide the lines
poem_1 = """This is all combined    
as one happy string... 
what was the sound
it was the door bell
When i see you, my heart sing"""
print(poem_1)                           #using \ we can brig the below line to above
poem_2 = """This is all combined \
as one happy string... 
what was the sound
it was the door bell \
When i see you, my heart sing"""
print(poem_2)
print(poem[1])
print(poem[10])
print(poem[50])
print(poem[20:])
print(poem[0:])
print(poem[:60 ])
print(poem[5:7])
set = "where am i?"
print(set[6:8])
print(set[6:-3])
start = 6
print(set[start:start+4]) #give character from start declared to number declared
name = "Umesh Mushkam"
start_of_last = 6
print(name[start_of_last:start_of_last+7]) #from 7th to whatever is added in print
print(name[6:])       #This is the example where print start from 7th letter
print(id(name))
print(id(set))
task = "Subcribe"
print(task)
print(id(task))
#task = task + "i"
different = task
different = "hey"
print(task)
print(id(task))
task = ["subcribe"]
different = task
different[0] = "hey"
print(task)
print(id(task))
msg = "please subscribe"
print(msg[:16])
print(msg[15])
print(len(msg))
print(msg[len(msg)-1])
#print("Your message contains" + len(msg) + "characters in it") #here we need to convert int to string using str()
print("Your message contains " + str(len(msg)) + " characters in it")
print("Your message contains", len(msg), "characters in it")
age = 15
print(len(str(id(str(age)) + math.floor(2.6))))
print(str(age))
print(id(str(age))) 
#print(str(id(str(age))))
print(math.floor(2.6))
print(str(str(id(str(age)) + math.floor(2.6))))
print(len(str(str(id(str(age)) + math.floor(2.6)))))

import math
age = 2000
age_str = str(age)
id_age_str = id(age_str)
other = math.floor(2.6)
other_1 = math.ceil(2.6)
added = id_age_str + other + other_1
added_str = str(added)
length = len(added_str)
print(age)
print(age_str)
print(id_age_str)
print(other)
print(other_1)
print(added_str)
print(length)
cant_change = "Java is my favorite"
new = 'K' + cant_change[1:]
print(new)
print(cant_change[5:])
fav_lang = "Python " + cant_change[5:]
print(fav_lang)
fav_lang_1 = "Python " + cant_change[:-15]
print(fav_lang_1)
fav_lang_2 = "Python " + cant_change[:15]
print(fav_lang_2)

#creating a list of int,strings and nestedlist

age = [12, 20, 76, 30]
people = ["john", "Raju", "ram", "pavan"]
my_fav_things = ["working out", 420, ['amazon prime', 'netflix', 'Gaming']]
print(age)
print(people)
print(my_fav_things)
my_fav_things[0] = "Walking"
print(my_fav_things)
x= len(my_fav_things)
print(x)

my_fav_things_1 = ["working out", 420, ['amazon prime', 'netflix', 'Gaming']]
copy = my_fav_things_1[:]   #make sure you copy a list[:] or my_fav_thing_1.copy()
print(copy)
copy[0] = "walking"
print(copy)
print(my_fav_things_1 , copy)
print(id(copy))
print(id(my_fav_things_1))
my_fav_things_2 = ["working out", 420, ['amazon prime', ['netflix', 'Gaming']]]
print(my_fav_things_2[2])
print(my_fav_things_2[2][1])
print(my_fav_things_2[2][1][0])
print(len(my_fav_things_2[2][1][0]))
print(len(my_fav_things_2[2][1]))

#work on c = copy.deepcopy(my_fav_thing)

print(my_fav_things_1 + my_fav_things_2)

my_fav_things.append("editing")
print(my_fav_things)

'''
print("Hey what your name?")
name = input()
print("Hello " + name + "How are you doing " + name)
print("How old are you ?")
age = input()
print("I am " + age)
print("Whats your fav number")
num = int(input())
print("Give us the other number")
num_1 = int(input())
print(num + num_1)
print("Hey the sum of your fav number is " + str(num + num_1))
print(str(num) + "+" + str(num_1) + "=" + str(num + num_1))
#print(num + "+" + num_1 + "=" + str(num + num_1)) 
# 
# '''
"""
under_age = 15
limmit = under_age > 20
print(limmit)

print("Please enter your age")
age_new = int(input())
if age_new > 65:
    print("Hey you are eligiable for special discount")
elif age_new == 21:
    print("You are the most sepical custmore")
elif age_new > 20:
    print("Welcome to our application")
else:
    print("You are not old enough")
    
print("Thanks for visiting")

"""
"""
happy = False
if happy:
    print("yay")
else:
    print(":-(")

print("Please enter your name")
name_1 = str(input())
if name_1 == "umesh" or name_1 == "mushkam":
    print("welcome " + name_1 + " you are in the database")
else:
    print("Sorry you dont have access to the site")

"""
subcribed = False
points = 50

if subcribed and points > 30:
    print("welcome")
    points -= 30
    print("Points now : ", points)

if not subcribed:
    print("Redirecting to the next page")
print(not subcribed)

















































































