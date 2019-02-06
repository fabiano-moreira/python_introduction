"""
Write a program to convert a temperature ºC in ºF.
Formula is:
F = 9 X C / 5 + 32
"""
temperature_celsius = int(input('What is the temperature in ºC: '))
temperature_fahrenheit = (((9 * temperature_celsius) / 5) +32)
print('The temperature after conversion is: %5.2fºF' % temperature_fahrenheit)


