def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"

print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

subjects = int(input("Enter Number of Subjects: "))

total = 0

for i in range(subjects):
    mark = float(input(f"Enter Marks for Subject {i+1}: "))
    total += mark

average = total / subjects
grade = calculate_grade(average)

print("\n===== Result =====")
print("Student Name :", name)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Grade        :", grade)