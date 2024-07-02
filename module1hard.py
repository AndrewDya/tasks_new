# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали
# подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит
# автоматизировать этот процесс":
#
# На вход даны следующие даннные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность
# имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
#
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
#
#
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).


# Первая версия
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students_list = sorted(list(students))
# students_grades = {}
# count, avr = 0, 0
# avr_list = []
#
# for grade in grades:
#     for i in grade:
#         count += 1
#         avr += i
#     avr_a = round(avr / count, 2)
#     count, avr = 0, 0
#     avr_list.append(avr_a)
#
# list_students_tuple = list(zip(avr_list, students_list))
#
# for item in list_students_tuple:
#     students_grades[item[1]] = item[0]
#
# print(students_grades)


# Вторая версия
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
students_grades = {}

for student, grade in zip(students_list, grades):
    average_grade = sum(grade) / len(grade)
    students_grades[student] = round(average_grade, 2)

print(students_grades)

