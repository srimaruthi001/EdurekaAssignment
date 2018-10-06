class Car(object):
    touch=10
    def __init__(self,a):
        self.a = a

    def getA(self):
        self.a = input("Please enter value")
    
    def putA(self):
        print(self.a,"is the value")
        print(touch+1)

class Maruti(Car):
    def __init__(self,b):
        self.b=b

    def getB(self,b):
        self.b = input("Please enter b")
    def putA(self):
        print(self.b,"is the value for b")

objA=Car()
objA.getA()
objB=Maruti()

