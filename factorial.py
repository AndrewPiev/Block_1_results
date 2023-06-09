number = int(input('Введите число: '))

factorial = 1
a = 0

while a < number:
    a +=1
    factorial *=a

print(factorial)


# Другой вариант:
# while number > 1:
#     factorial = factorial * number
#     number = number - 1

# print(factorial)