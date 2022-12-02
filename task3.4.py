# Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Enter number: '))
a = ' '

def transform(dano: int, isk: int):      # прошу прощения за переменные, мне так проще сообразить было)
    while dano > 0:
        isk = str(dano % 2) + isk
        dano = dano // 2
    print(isk)

transform(n, a)