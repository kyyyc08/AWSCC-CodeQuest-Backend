with open('names.txt', 'r') as file:
    students = file.readlines()
    sorted_names = sorted(students)

with open('names.txt', 'w') as file:
    for name in sorted_names:
        file.write(name.strip() + '\n')