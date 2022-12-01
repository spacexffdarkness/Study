students = int(input('Enter the number of students:'))
apples = int(input('Enter the number of apples: '))
apples_for_students = apples // students
print(str(apples_for_students)+ ' apples for every student')
apples_in_basket = apples % students
print(str(apples_in_basket) + ' apples stay in basket')


