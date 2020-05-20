# Task_1.  Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.


a = int(input("Введіть число "))
b = int(input("Введіть число "))
if a == b:
    print("Числа {0} і {1} рівні".format(a, b))
elif a <= b:
    мін_зн, макс_зн = a, b
    print("Число {0} - мінімальне число , а число {1} - максимальне число".format(мін_зн, макс_зн))
else:
    мін_зн, макс_зн = b, a
    print("Число {0} - мінімальне число , а число {1} - максимальне число".format(мін_зн, макс_зн))
print()


# Task_2.  Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.


num = int(input("Enter a number: "))
if num % 2 == 0:
   print("The number {0} is even".format(num))
else:
   print("The number {0} is odd".format(num))
print()


# Task_3.  Написати скрипт, який обчислить факторіал введеного числа.


n = int(input('Введіть число: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print('Факторіал числа {} становить'.format(n), factorial)
print()
