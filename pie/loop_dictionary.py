student_grades = {"Marry": 9.1, "Josh": 8.1, "Drake": 5.5}

# for grades in student_grades.values():
#     print(grades)

for key, value in student_grades.items():
    print('{}: {}'.format(key, value))
