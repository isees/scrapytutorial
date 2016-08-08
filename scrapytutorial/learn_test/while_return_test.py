import random


def get_lower_number(number, max):
    while number < max:
        number += 1
        return number


x = get_lower_number(1, 10)
print x


def while_pop(array):
    while array != []:
        print array.pop()


array = []
# while array.__len__() < 10:
#     array.append(random.randint(1, 100))

for i in range(1, 10):
    array.append(random.randint(1, 100))

print array
while_pop(array)
