# Program for entering student details and calculating total, average, and grade

student_name = input("Enter student name: ")

mark_sub1 = int(input("Subject 1 marks = "))
if mark_sub1 < 0 or mark_sub1 > 100:
    print("Error: Invalid entry")
    exit()

mark_sub2 = int(input("Subject 2 marks = "))
if mark_sub2 < 0 or mark_sub2 > 100:
    print("Error: Invalid entry")
    exit()

mark_sub3 = int(input("Subject 3 marks = "))
if mark_sub3 < 0 or mark_sub3 > 100:
    print("Error: Invalid entry")
    exit()

total_marks = mark_sub1 + mark_sub2 + mark_sub3
average_marks = total_marks / 3

print("\nStudent Name:", student_name)
print("Total Marks =", total_marks)
print("Average Marks =", average_marks)

if average_marks >= 90:
    print("Grade A awarded")
elif average_marks >= 80:
    print("Grade B awarded")
elif average_marks >= 70:
    print("Grade C awarded")
elif average_marks >= 60:
    print("Grade D awarded")
elif average_marks >= 50:
    print("Grade E awarded")
else:
    print("Grade F awarded")
