# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.



class Student():
    def __init__(self,name,marks) -> None:
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name: {self.name} ,Marks: {self.marks}") 

s1=Student("Alice",30)  
s1.display()         
        