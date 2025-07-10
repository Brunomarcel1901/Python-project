score = int(input("Enter Score:"))
grade = ''
if score in range (0,39):
    grade = 'F'
elif score in range (40,44):
    grade = 'E'
elif score in range (45,49):
    grade = 'D'
elif score in range (50,59):
    grade = 'C'
elif score in range (60, 69):
    grade = 'B'
elif score in range (70, 100):
    grade = 'A'
else:
    grade = 'Your input is invalid'
print(grade)