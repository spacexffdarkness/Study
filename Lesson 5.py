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
h = int(input('Please, type the number of hight: '))
for g in range(h):
    for w in range(g):
        print('*', end=' ')
    print()
# B
# C
# D
