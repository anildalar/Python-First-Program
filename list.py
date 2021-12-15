students = []

scount = input("Please  the no of students ")

scount = int(scount)


for x in range(scount): # 0 < scount 0 < 4 or 0 <= 3
    student = input("Please Enter the student name  ")
    students.append(student)

print(students)

for y in students:
    print(f"Hello {y}, How are yoy")