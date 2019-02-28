print ("Hello world")
#Hello World
""" This is a
multiline comment """
my_array = [1,2,3,4,5]

for number in my_array:
    if number % 3 == 0:
        print (number*2)
    else:
        print (number)

def AddTwo(x,const = 2):
    return x+2

print (AddTwo(10))


def MyClass():
    common = 10
    def __init__(self):
        self.myvariable = 5
    def myfunction(arg1,arg2,self):
        return self.myvariable

x = MyClass()
x.myfunction(1,2,3)
