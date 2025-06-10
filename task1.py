# Задание 1. Создайте список с 10-ю именами. Выведите из этого списка имена начинающиеся
# на А;

name_list = ['Anton', 'Alexander', 'Andrew', 'Anna', 'Xur', 'Kirill', 'Steve', 'Dexter', 'Sharik']

print(f'{name_list}\n')
print('Имена, начинающиеся на А:', end=' ')
for i in name_list:
    if i[0] == 'A':
        print(f'{i}', end=' ')
