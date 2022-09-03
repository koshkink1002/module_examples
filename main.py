# import numbers_functions
from numbers_functions import summa_of_two, production, division
from numbers_functions import substruction_of_two as olds_substructions


a = float(input("Введите число А "))
b = float(input("Введите число B "))

summa = summa_of_two(a, b)
print(summa)

dif = olds_substructions(a, b)
print(dif)

prod = production(a, b)
print(prod)

div = division(a, b)
print(div)
