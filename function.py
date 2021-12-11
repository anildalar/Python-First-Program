# is a single line comment
#1. Hello Every

'''
  is a multiline comment
    Hello everyone
    How are you you
    We are learning Python
'''

# name is a variable 
# variable can store values

name='ANIL'
name2="POONUM"
name3=""" Avadhi """

'''
print(name)
print(name2)
print(name3)

'''


# We can create a function

#1. Function Defination
def greet(n,s): # n is formal argument
    print(type(s))
    s = str(s) # type casting  int ---> string
    print(type(s))
    print('Hello '+n+', How are you? Your salary is '+s)

#2. FUnction calling
greet('ANIL',10000) # 'Anil' Is a actual Arguments
greet("Poonum",15000)
greet("""Avadhi""",20000)




#1. Function defination
# String Interpolation/Substitution
def hello(n,s): #camelCase
    print(f"Hello {n},How are you? Your salary is {s}")

#2. Function calling
hello('ANIL',30000)

def myFunction(): #
    pass