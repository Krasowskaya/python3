# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


numbers = [1.1, 1.2, 3.1, 10.01]
result = list()

def find(numb: list,res: list):
    for i in range(len(numb)):
        n = round((float(numb[i]) - int(numb[i])),2)
        res.append(n)
        i += 1
    return print(result)

def find_diff(lst: list):
    max = 0
    min = ''
    for i in range(len(lst)):
        if float(lst[i]) > max:
            max = float(lst[i])
            min = float(lst[i])
        elif float(lst[i]) < min:
            min = float(lst[i])
            i += 1
    print(max - min)

find(numbers,result)
find_diff(result)


























exit()
def find_fract (lst: list, st: str,result: list):
    #result = list()
    for i in range(len(lst)):
        res = str(lst[i]).split(st)
        result.append(res[1])
        i +=1
    print(result)

find_fract(numbers, s, result)



def find_diff(lst: list, max: int=0):
    # max = 0
    # min = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
        elif lst[i] < min:
            min = lst[i]
        else:
            i += 1
    print(max,min)

find_diff(result)