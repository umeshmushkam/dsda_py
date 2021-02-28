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
        return lst

a=10000000

t1 =time.time()
sum(OddGen(1,a))
print("Time to sum OddGen: %f" %(time.time() -t1))

t1 =time.time()
sum(OddLst(1,a))
print("Time to sum Lst: %f" %(time.time() -t1))
