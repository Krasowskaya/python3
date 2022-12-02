# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = (2, 3, 4, 5, 6)

def find_prod(numb: list):
    result = list()
    if int(len(numb)) % 2 == 0:
        for i in range(int(len(numb)/2)):
            prod = numb[i] * numb[len(numb) - 1 - i]
            result.append(prod)
            i += 1
    else:
       for i in range(int(len(numb)/2) + 1):
            prod = numb[i] * numb[len(numb) - 1 - i]
            result.append(prod)
            i += 1
    print(result) 

find_prod(numbers)