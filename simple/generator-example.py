# compares run time
import time

# generator function creates an iterator of odd numbers in n.m

def OddGen(n,m):
    while n < m:
        yield n
        n += 2

#  builds a list of add numbers n and m

def OddLst(n,m):
    lst=[]
    while n < m:
        lst.append(n)
        n +=2
    return lst

a=10000

t1 =time.time()
sn = sum(OddGen(1,a))
print(sn)
print("Time to sum OddGen: %f" %(time.time() -t1))

t1 =time.time()
sn = sum(OddLst(1,a))
print(sn)
print("Time to sum Lst: %f" %(time.time() -t1))
