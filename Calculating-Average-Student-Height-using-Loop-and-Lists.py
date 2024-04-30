student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(f"\nThe list of student height is: {student_heights}")

total_height = 0
for height in student_heights:
    total_height = total_height + height
print(f"The sum of total student height is: {total_height}")

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(f"The length of total student height is: {number_of_student}")

average_height = round(total_height/number_of_student)
print(f"Average height of a student is: {average_height}")