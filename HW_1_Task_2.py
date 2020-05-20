###   task_2_a   ###

print("What is your name?")
name = input('Input your name: ')
print("How old are you?")
age = input('Input your age: ')
print("Where do you live?")
city = input('Input your city: ')
print("Hello, ", name, "! Your age is ", age, ". You live in ", city, ".", sep='')
print()
###   task_1_b   ###

print("What is your name?")
name = input('Input your name: ')
print("How old are you?")
age = input('Input your age: ')
print("Where do you live?")
city = input('Input your city: ')
answer = "Hello, {}! Your age is {}. Your live in {}."
print(answer.format(name, age, city))
print()