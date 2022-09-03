# import numbers_funcions
from numbers_funcions import summa_of_two
from numbers_funcions import subsrtuction_of_two as olds_substructions


a = float(input("Введите число А "))
b = float(input("Введите число B "))

summa = summa_of_two(a, b)
print(summa)

dif = olds_substructions(a, b)
print(dif)
