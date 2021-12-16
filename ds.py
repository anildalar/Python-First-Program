# from somelibrary import something
from string import Template
#DS = Data Structure 

# Python DS

#1. LIST []
# List is variable which can store more than one value of differenct data type at a time

#friend is normal variable
#normal variable can only store one value at a time.

friend = 'ANIL'
friend = 'SUNIL' # Previous value will be overwritten

print(friend)

# 1. LIST []
# Note: List is a interable item


students = ['ANIL',"SUNIL","Deepak",3000,30.50,True]

count = len(students)

print(count)

# How we can get the length of a list ?

'''
    for singular in plural:

    for anyvariable in iterables:


'''
for student in students:
    # I am using a string interpolation method
    print("Hello {}, How are you".format(student))

for indexno in range(count):

    #print(f"Hello {students[indexno]}, How are you ?")
    print("Hello %s and %s, How are you ?"%(students[indexno],"Poonum"))



# Dictionaray
'''  "key":value  '''
friends = {
    
    "name":'ANIL',
    "salary":3000,
    "age":30.5
}
'''  "key":value  '''


print(friends["name"])

for y in friends:
    #print(y)  -- Key
    #print(y)  # dictionary["key"] = value
    print(friends[y])
    n = Template('Hello $n3 , How are you? ')
 
    # and pass the parameters into the template string.
    print(n.substitute(n3=friends[y]))