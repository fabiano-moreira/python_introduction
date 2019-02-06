"""
Calculate an estimated time to complete a car trip.
Ask the distance to finish and the average speed expected.
"""

distance = float(input('Please, inform the distance in km: '))
average_speed = float(input('Inform the average speed in km/h: '))
travel_time = (distance / average_speed)
print('The estimated time are %5.2f' %travel_time)
