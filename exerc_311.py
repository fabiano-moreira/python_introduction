"""
Create a program that asks the price of a product and the discount percentage.
And show the discount and the final price.
"""
product_price = float(input('Enter the product price: '))
discount_percentage = int(input('Please enter product discount percentage: '))
discount_final = ((product_price * discount_percentage) / 100)
final_price =  (product_price - discount_final)
print('The product discount are %5.2f' % discount_final, 'and the final product price are %5.2f' %final_price)
