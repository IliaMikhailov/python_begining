season_list = ['зима', 'весна', 'лето', 'осень']
user_number = int(input('Введите число от 1 до 12: '))
if user_number == 12 or user_number == 1 or user_number == 2:
    print(season_list[0])
elif user_number == 3 or user_number == 4 or user_number == 5:
    print(season_list[1])
elif user_number == 6 or user_number == 7 or user_number == 8:
    print(season_list[2])
elif user_number == 9 or user_number == 10 or user_number == 11:
    print(season_list[3])

# Решение с изпользованием словаря

season_list_dict = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
print(season_list_dict[user_number])