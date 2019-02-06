"""
Calculate the reduce life time for a smoke person.
How many cigarettes per day and how many years smoking.
Less 10 minutes life after one cigarette.
How many days are loose.
"""
smoke_day = int(input('How many cigarettes per day? '))
smoke_year = float(input('How many years smoking? '))
time_calc = ((smoke_year * 365) * (smoke_day * 10))
time_loose = (time_calc / (60 * 24))
print('You have %5.2f days' % time_loose)



