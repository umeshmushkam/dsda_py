# healthy = ["salad","Veggies","braccoli"]
# healthy.append("fruits")
# healthy.append("coco")
# length = len(healthy)
# print(healthy)
# print("length", length)

# print("chicken pot pie" in healthy)


# carry = ["Chips","broccoli","fruits"]
# bagpack = ["pizza","burger","apple","fruits"]
# if "fruits" not in carry:
#     bagpack.remove("fruits")
# print(bagpack)


# for names in carry:
#     statment = " ".join(["I eat " , names])
#     print(statment)
#     print(",".join(carry))

# who = "Umesh"
# how_many = 10
# print("{} bought {} apples today !!!" .format( who , how_many))

# def calc(x, y, ops):
#     if ops == "add":
#         return x + y
#     elif ops == "sub":
#         return x - y
#     elif ops == "mul":
#         return x * y
#     elif ops == "div":
#         return x / y

# ops = calc(10,2, 'sub')
# print(ops)

# import os            #to read the file from the directory
# >>> location_of_file = '/Users/umeshmushkam/Documents'
# >>> file_name = 'test.txt'
# >>> with open(os.path.join(location_of_file, file_name)) as f:
# ...     print(f.read())


# import argparse
# import sys

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help='What is the first number?')
#     parser.add_argument('--y', type=float, default=1.0,
#                         help='What is the second number?')
#     parser.add_argument('--operation', type=str, default='add',
#                         help='What operation? Can choose add, sub, mul, or div')
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))



# xyz = (i for i in range(50000000))
# print(list(xyz)[:100])


# xyz = [i for i in range(50000000)]
# print(xyz[:5])















