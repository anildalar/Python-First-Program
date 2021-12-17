# We can export anything
#1. Function
def hello(name):
    print("Hello {},How are you ?".format(name))


#2. Class

class MyClass():
    #1. Property
    #2. Constructor
    #3. Method
    def sayHello(self,name):
        print(f"Hello {name},How are you")


#

#3. Class Object
myclassobject = MyClass()

#4. LIST []

students = ['A','B','C','D','E','F','G','H','I','J','K','L']

#5. Dictionaray

friend = {
    "name":"John",
    "Country":"USA",
}

class Parent():
    #1. Property
    #2. Constructor
    #3. Method
    def sayHelloParent(self):
        print(f"Parent Method")


class Child(Parent):
    #1. Property
    #2. Constructor
    #3. Method
    def sayHelloChild(self):
        print(f"Child Method")




o = Child()