# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank():
    bank_name="Allied Bank"

    @classmethod
    def change_bank_name(cls,name):
         cls.bank_name=name
b1=Bank()   
b2=Bank()
Bank.change_bank_name("Habib Bank ")   
print(b1.bank_name)  
print(b2.bank_name) 
