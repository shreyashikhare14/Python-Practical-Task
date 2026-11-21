"""
        Mini Project 2: Student Marks and Grade Report
"""

while True:
    num_students = int(input("Enter a Number of Student = "))

    if num_students > 0:
        break
    else:
        print("Please enter a valid number of students.")


total =0
pass_count =0
fail_count = 0

for i in range(1,num_students + 1):
    name = input("Enter a Name of Student =")

    while True:
        marks  = int(input("Enter a Student marks ="))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 to 100.")
    total = total + marks

    if marks >=75:
        grade = 'A'

    elif marks >=60 :
        grade = 'B'

    elif marks >=50:
        grade = 'C'

    elif marks >=40:
        grade = 'D'

    else:
        grade = 'Fail'

    if marks >=40:
        pass_count = pass_count + 1

    else:
        fail_count = fail_count + 1

    print(name,"Grade =",grade)

average = total / num_students

print("Class Average =", average)
print("Total Pass Students =", pass_count)
print("Total Fail Students =", fail_count)
print("Total Marks =", total)

    
    

    





