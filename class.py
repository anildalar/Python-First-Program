

#1. Class Defination
class MyClass:  #PascalCase
    #1. Property
    #2. Constructor
    #3. Method
    def hello(self,n,s=10000): #camelCase #default value
        print(f"Hello {n},How are you? Your salary is {s}")

#2. Create the object of the class

# objectname = ClassName()

o = MyClass()

# objectname.membername
o.hello("ANIL",20000)