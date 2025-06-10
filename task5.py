# Задание 5. Дан символ С и строковая последовательность А. Найти количество элементов
# А, которые содержат более одного символа и при этом начинаются и оканчиваются символом
# С;

C = 'a'
A = ['abc', 'amavma', 'efga' 'sphere', 'pyramid']

def task5(string_array, symbol):
    result = 0
    for i in range(len(string_array)):
        if len(string_array[i]) < 2:
            continue
        elif string_array[i][0] and string_array[i][-1] == symbol:
            result += 1
    return result

print(f'{A}\nНайдено {task5(A, C)} строк более одного символа, которые начинаются и оканчиваются на "{C}"')
