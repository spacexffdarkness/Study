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
for x in range(2, simple_num//2 + 1):
    if simple_num % x == 0:
        print('That\'s not simple number')
        break
    else:
        print('That\'s simple number')
