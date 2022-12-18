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
h_a_in = int(input('Please, type the height number of A-figure: '))
x = 0
if h_a_in == 1:    # That's look like a bad solution
    h_a_in = 0
else:
    pass
h_a = h_a_in - 1

for j in range(1, h_a + 1):
    print(end='  ')
    for emptiness in range(1, (h_a - j) + 1):
        print(end="  ")

    while x != (2*j) - 1:
        u = '*' + ' ' * (x * 2)
        print(u, end=' ')
        x += 1

    print()

print('* ' * (h_a * 2 + 1))


# B
h_b = int(input('Please, type the height number of B-figure: '))
c = 0
for i in range(1, h_b + 1):
    for empty in range(1, (h_b - i) + 1):
        print(end="  ")

    while c != (2*i) - 1:
        print('* ', end='')
        c += 1

    c = 0
    print()


# C  (This is not complete)
h_c = int(input('Please, type the height number of C-figure: ')) // 2
trian = 0
for q in range(1, h_c + 1):
    for e in range(1, (h_c - q) + 1):
        print(end="  ")

    while trian != (2 * q) - 1:
        print('* ', end='')
        trian += 1

    trian = 0
    print()
d_t = h_c -1
for d_q in range(h_c, 1, -1):
    # print(" " * (d_q * 2) + '*', end="")
    for d_e in range(d_q):
        print('*', end='')
    print()
# D
