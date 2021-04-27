# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_1 = input("Введите число: ")
print("Количество символов: ", len(number_1))
i = 0
max_num = 0
while i < len(number_1):
    letter = number_1[i]
    letter = int(letter)
    if max_num < letter:
        max_num = letter
#        print("Максимальное число на данный момент равно:", max_num)
#    else:
#        print("Число меньше или равно максимальному!", letter)
    i += 1
print("Итоговое максимальное число равно:", max_num)