# classes initialize

class Employee(object):
    numEmployee = 0
    def __init__(self,name,rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1
    
    def __del__(self):
        Employee.numEmployee -= 1
    
    def hours(self, numHours):
        self.owed += self.rate * numHours
        return ("%s worked %.2f hours and company owes %.2f" % (self.name, numHours, self.owed))
    
    def pay(self):
        if self.owed == 0:
            res =  "company owes %.2f amount. so Napyment is processed" % self.owed
        else:
            res = "company paid %.2f" % self.owed
            self.owed = 0
        return res

class specialEmployee(Employee):
    def __init__(self,name,rate,bonus):
        Employee.__init__(self,name,rate) # calls base class
        self.bonus = bonus

    def hours(self,numHours):
        self.owed += self.rate * numHours * 2 + self.bonus
        return ("%s worked %.2f hours and company owes %.2f" % (self.name, numHours, self.owed))


emp1 = Employee("ravi", 30)
emp2 = Employee("umesh", 33)
emp3 = specialEmployee("ravikanth", 30, 1000)
Employee.numEmployee

print(emp1.hours(160))
print(emp2.hours(99))
print(emp3.hours(160))

print(emp1.pay())
print(emp1.pay())

# print(dir(emp1))