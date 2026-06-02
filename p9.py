# Student Grade Tracker
students = {}
n = int(input("Enter number of students: "))
# Input student details
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
# Summary calculations
total_marks = sum(students.values())
average = total_marks / n
topper = max(students, key=students.get)
highest = students[topper]
lowest_student = min(students, key=students.get)
lowest = students[lowest_student]
# Display results
print("\n----- Student Report -----")
for name, marks in students.items():
print(name, ":", marks)
print("\nClass Average:", average)
print("Topper:", topper, "-", highest)
print("Lowest Score:", lowest_student, "-", lowest)
