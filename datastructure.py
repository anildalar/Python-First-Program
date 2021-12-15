
# String
x = "OKLABS"
y = 40000.00
z = 'ANIL'

a = """ Avadhi """
b = ''' Deepak '''

''' Manish ''' # Comments

print(type(x))

print(type(y))

print(type(z))

print(type(a))

print(type(b))


students = ['Deepak',"Manish",""" Devendra """,''' Poonum '''] # List

print(type(students))

print(students[0])

print("The Total Students are {} ".format( len(students) ) )

print("Hello {} and {}, How are you ?".format(z,a))

c = input("Please Enter the number ") # 3.6 Python 

print(f"Before TypeCast {type(c)} ") # f-string interpolation 3.6 Python

c = int(c) # Type Cast  string ---> integer

print(f"After TypeCast {type(c)} ")

if c == 3000:
    print("c is equal to 3000")
else:
    print("c is not equal to 3000")


