tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
#help("len")
#checkpoint1
"""
Create a variable called max_price and call the built-in function max() with the variables of prices to get the maximum price.

Print max_price.
"""
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
print("Maximum price is: " + str(max_price))

#checkpoint2
"""
Using the same set of prices, create a new variable called min_price and use the built-in function min() with the variables of prices to get the minimum price.

Print min_price.
"""
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
print("Minimum price is: " + str(min_price))

#checkpoint3
"""
Use the built-in function round() to round the price of the variable tshirt_price by one decimal place.

Save the result to a variable called rounded_price and print it.
"""
rounded_price = round(tshirt_price, 1)
print(rounded_price)
print("The rounded price of T-Shirt is: " + str(rounded_price))