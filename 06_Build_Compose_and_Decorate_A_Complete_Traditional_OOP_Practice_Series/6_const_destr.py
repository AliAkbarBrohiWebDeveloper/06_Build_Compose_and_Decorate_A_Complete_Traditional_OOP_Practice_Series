# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger():
    def __init__(self) :
        print("Logger initialized")
       

    def __del__(self):
        print("Logger is Destroyed")

log=Logger()       
del log