"""
Создать список состоящий из отдельных единичных символов, преобразовать список в строку, инвертировать строку и
вывести на печать.
"""

my_list = ["m", "y", "_", "l", "i", "s", "t"]

my_str = "".join(my_list)

print(my_str[::-1])
