# Given a list of prices, add 10 to the price if it is greater than 50, otherwise add 2. Use a lambda function and the map() function to achieve this.

prices = [25.0, 62.0, 15.0, 80.0, 45.0]
price_fifty = lambda x: x+10 if x>50 else x+2
final_prices = map(price_fifty, prices)
print(list(final_prices))