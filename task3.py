# Задание 3. Создайте класс Task описывающий занятие, с свойствами: DateStart, DateFinish,
# Description. Создайте список объектов Task из 5 элементов. Выведите информацию о занятии
# заканчивающемся позже всех, если таких занятий несколько, выведите первое подходящее
# под условие;

import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

class Task:
    def __init__(self, start, finish, description):

        start = list(map(int, start.split('.')))
        self.DateStart = datetime.date(start[2], start[1], start[0])

        finish = list(map(int, finish.split('.')))
        self.DateFinish = datetime.date(finish[2], finish[1], finish[0])

        self.Description = str(description)


test1 = Task('01.01.2024', '07.03.2024', 'Математика')
test2 = Task('01.01.2024', '31.01.2024', 'Физика')
test3 = Task('01.01.2024', '30.06.2024', 'Химия')
test4 = Task('01.01.2024', '05.02.2024', 'Проектная деятельность')
test5 = Task('01.01.2024', '30.06.2024', 'Биология')

tasks = [test1, test2, test3, test4, test5]
dates_finish = list(i.DateFinish for i in tasks)
result = tasks[dates_finish.index(max(dates_finish))]

print(f"{result.Description} "
      f"({result.DateStart.strftime('%d %B %Y')} - {result.DateFinish.strftime('%d %B %Y')})")
