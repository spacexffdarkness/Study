# first task
students = int(input('Enter the number of students:'))
apples = int(input('Enter the number of apples: '))
apples_for_students = apples // students
print(str(apples_for_students) + ' apples for every student')
apples_in_basket = apples % students
print(str(apples_in_basket) + ' apples stay in basket')

# another task
a_group = int(input('Enter the number of students in A-group')) + 1
b_group = int(input('Enter the number of students in B-group')) + 1
c_group = int(input('Enter the number of students in C-group')) + 1
print(f'The number of desks is { a_group // 2 + b_group // 2 + c_group // 2}')


# different another task
the_number = int(input('Enter three-digit number'))
a_num = the_number // 100
b_num = the_number // 10 * 10
c_num = the_number % 10 - a_num
print(c_num * 100 + b_num + a_num)

# something else
seconds = int(input('Enter the number of seconds'))
sec = seconds % 60
mid_res = seconds // 60
hours = mid_res // 60
minutes = mid_res % 60
print(f'{hours}:{minutes}:{sec}')
