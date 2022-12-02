# Задайте число. Составьте список чисел Фибоначчи, в
#  том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


k = int(input('Enter number-->'))
print(list(fib(k)))







exit()
def fibonacci(n):

    if n in range(0,2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

k = int(input('Enter number: '))
print(fibonacci(k))
















exit()
def fibo(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return (fibo(n - 1) + fibo(n - 2))
        
fibo(k)