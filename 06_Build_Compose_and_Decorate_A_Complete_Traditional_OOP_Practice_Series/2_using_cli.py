# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter():
    counter=0
    def __init__(self):
      Counter.counter+=1
    @classmethod
    def show_count(cls):
         print(f"Total Objects {cls.counter}")

count=Counter()
C1=Counter()  
C2=Counter() 
print(Counter.show_count()  )   

         