# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee():
    def __init__(self,name,salary,ssn):
        self.name=name
        self._salary=salary
        self.__ssn=ssn

e1=Employee("Ahmad",30000,"124-35-6784")   
print(e1.name)    
print(e1._salary) 


try:
    print("pruvate",e1.__ssn)
except AttributeError as e:
    print("Private cannot access directly",e)


print("Private using name mangling :", e1._Employee__ssn)    