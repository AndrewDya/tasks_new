immutable_var = (1, 2, "new_value", [5, 6])
print(immutable_var)
# immutable_var[0] = 5 TypeError: 'tuple' object does not support item assignment
# tuple встроенный неизменяемый класс, не поддерживает методы изменения элементов (магических тоже нет)

mutable_list = [x ** 2 for x in range(1, 6)]
print(mutable_list)
mutable_list[0], mutable_list[1] = 2, 6
print(mutable_list)