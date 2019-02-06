"""
Write a program for read how many days, hours, minutes and seconds and calculate the total in seconds
"""

total_days = int(input('Write the number of days to convert: '))
total_hours = int(input('Write the number of hours to convert: '))
total_minutes = int(input('Write the minutes to convert: '))
total_seconds = int(input('Write the seconds to convert: '))
days_to_seconds = (total_days * 86400)
hours_to_seconds = (total_hours * 3600)
minutes_to_seconds = (total_minutes * 60)
converted_seconds = (days_to_seconds + hours_to_seconds + minutes_to_seconds + total_seconds)
print('The hole time in seconds are: ', converted_seconds, 's')
