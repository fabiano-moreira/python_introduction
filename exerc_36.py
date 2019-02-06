"""
Write an expression to decide whether or not a student will pass.
The approved student must have a average grade above 7.
The student attends only three classes.
class1, class2, and class3
"""
class1 = 10
class2 = 5
class3 = 7
average = ((class1 + class2 + class3) / 3)
approved = average > 7
if approved == True:
    print('The student was approved')
else:
    print('The student was not approved')
