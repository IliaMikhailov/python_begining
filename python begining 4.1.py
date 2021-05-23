from sys import argv

hours_worked = int(argv[1])
cost_hour = int(argv[2])
bonus = int(argv[3])
salary = hours_worked * cost_hour + bonus
print(salary)