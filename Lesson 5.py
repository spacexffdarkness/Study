# first task
my_string = '0123456789'
n = 0
i = 0
while i <= 9:
    num1 = my_string[i]
    i += 1
    for h in my_string:
        num2 = my_string[n]
        num = num1 + num2
        print(int(num))
        n += 1
        if n > 9:
            n = 0


# second task
# A
height_a = int(input('Please, type the height number: '))
i = 1


# height_a = int(input('Please, type the height number: '))
# for h in range(height_a):
#    for e in range(h):
#        empty = ' ' * (height_a//2)
#        print(empty, end='')
#    print('*')
# print("*\t" * height_a + '*')

# B
height_b = int(input('Please, type the height number: '))
for h in range(height_b):
    for e in range(h):
        empty = ' ' * (height_b//2)
        print(empty, end='')
    for w in range(h):
        print('*', end='')
    print('')

# height_a = int(input('Please, type the height number: '))
# for i in range(1, height_a + 1):
#    print('' * height_a, end='')
#    print('*' * i)
#    height_a -= 1
# C

# D
