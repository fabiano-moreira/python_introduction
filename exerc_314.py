"""
Create a program that asks how many kilometers a car has traveled and how many days this car has been rented.
Calculate the price of this rental car.
The cost of the car is $ 60.00 per day and $ 0.15 per km.
"""
traveled_kilometers = int(input('Inform how many kilometers this car travel: '))
days_rented = int(input('Enter how many days this car was rented: '))
price_car = ((days_rented * 60) + (traveled_kilometers * 0.15))
print('The total cost is $%7.2f' % price_car)
