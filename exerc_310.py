"""
Create a program that calculates the salary increase.
Ask for the salary and percentage increase.
Show the total of increase and the new salary.
"""
salary = int(input('Type your salary in integer numbers: '))
increase_percentage = int(input('Enter as a percentage how much your salary increases: '))
total_increase = ((salary * increase_percentage) / 100)
new_salary = (salary + total_increase)
print('You have a increase of %5.2f ' % total_increase, 'and you new salary is %5.2f' % new_salary)

