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
h_a = int(input('Please, type the height number: '))

# B
h_b = int(input('Please, type the height number: '))
c = 0
for i in range(1, h_b + 1):
    for empty in range(1, (h_b - i)+1):
        print(end="  ")

    while c !=(2*i) - 1:
        print('* ', end='')
        c += 1

    c = 0
    print()
# C

# D
