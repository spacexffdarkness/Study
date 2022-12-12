# first task
num1 = int(input('Type the first num: '))
act = input('Type your operation: ')
num2 = int(input('Type the second number: '))
if '+' in act:
    print(num1 + num2)
elif '-' in act:
    print(num1 - num2)
elif '*' in act:
    print(num1 * num2)
elif '/' in act:
    print(num1 / num2)
elif '**' in act:
    print(num1 ** num2)
else:
    print('Invalid operation')

# second task
i = 0
lim = int(input('Please, type the limit number: '))
for i in range(lim + 1):
    i = i ** 2
    if i < lim:
        print(i)


# third task
simple_num = int(input("Type the number: "))
if simple_num % 1 == 0 and simple_num % simple_num == 0:
    print('That\'s simple number')
else:
    print('Sorry, that\'s not simple number')