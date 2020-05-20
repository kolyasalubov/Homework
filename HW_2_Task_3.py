####____3____####

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної

y = input('Enter your first variable: ')
z = input('Enter your second variable: ')
print('Your first variable is: ', y)
print('Your second variable is: ', z)
y, z = z, y
print('Your variables have changed values')
print('Now your first variable is: ', y)
print('Now your second variable is: ', z)
