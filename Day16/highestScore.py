# This code calculates the total score of students and prints it.
student_score = [150, 200, 250, 300, 350, 400, 450, 500]
total_score = sum(student_score)
print(total_score)

# This code calculates the total score of students and prints it.
sum = 0
for score in student_score:
    sum += score
print(sum)

# This code finds the highest score among students and prints it.
max = 0
for score in student_score:
    if score > max:
        max = score
print(max)
