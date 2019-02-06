"""
Calculate the bonus per year
"""
year = int(input('Years of service: '))
value_per_year = float(input('Value per service year: '))
bonus = year * value_per_year
print('Bonus of $ %5.2f' % bonus)
