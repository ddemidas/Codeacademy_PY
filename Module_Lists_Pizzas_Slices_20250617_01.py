# Your code below:
before = "\nbefore: "
after = "\nafter: "

#checkpoint_1
#To keep track of the kinds of pizzas you sell, create a list called
toppings = [
  "pepperoni", 
  "pineapple", 
  "cheese", 
  "sausage", 
  "olives", 
  "anchovies", 
  "mushrooms"
  ]

print("checkpoint_1\nlist of pizzas we sell: ", toppings)

#checkpoint_2
#To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:

prices = [
  2, 
  6, 
  1, 
  3, 
  2, 
  7, 
  2
]

print("\ncheckpoint_2\nprices for our pizzas: ", prices)

#checkpoint_3
"""
Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
"""

num_two_dollar_slices = prices.count(2)
print("\ncheckpoint_3\nnumber of two dollar slices: ", num_two_dollar_slices)

#checkpoint_4
"""
Find the length of the toppings list and store it in a variable called num_pizzas.
"""
num_pizzas = len(toppings)
print("\ncheckpoint_4\nnumber of pizzas we sell: ", num_pizzas)

#checkpoint_5
"""
Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
"""

print("\ncheckpoint_5\nWe sell "+str(num_pizzas)+" different kinds of pizza!")

#checkpoint_6
#checkpoint_7
"""
Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.
"""

pizza_and_prices = [
  [2, "pepperoni"], 
  [6, "pineapple"], 
  [1, "cheese"], 
  [3, "sausage"], 
  [2, "olives"], 
  [7, "anchovies"], 
  [2, "mushrooms"]
]

print("\ncheckpoint_6_7\nall pizzas with prices: ", pizza_and_prices)

#checkpoint_8
"""
Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
"""
#sort wasn't easy, found it here:
#https://stackoverflow.com/questions/25046306/sort-a-2d-list-first-by-1st-column-and-then-by-2nd-column 
pizza_and_prices_sorted_by_price = sorted (
  pizza_and_prices,
  key=lambda x: (x[0],x[1])
)
print("\ncheckpoint_8\nall pizzas sorted by price: ", pizza_and_prices_sorted_by_price)

#checkpoint_9
"""
Store the first element of pizza_and_prices in a variable called cheapest_pizza.
"""
cheapest_pizza = pizza_and_prices_sorted_by_price[0]
print("\ncheckpoint_9\nthe cheapest pizza is: ", cheapest_pizza)

#checkpoint_10
"""
A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
"""
priciest_pizza = pizza_and_prices_sorted_by_price[-1]
print("\ncheckpoint_10\nthe most expensive pizza is: ", priciest_pizza)

#checkpoint_11
"""
It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
"""
print("\ncheckpoint_11", before, "the most expensive pizza is: ", priciest_pizza)
print("among these pizzas: \n", pizza_and_prices_sorted_by_price)
pizza_and_prices_sorted_by_price.pop()
priciest_pizza = pizza_and_prices_sorted_by_price[-1]
print(after, "the most expensive pizza is: ", priciest_pizza)
print("among these pizzas: \n", pizza_and_prices_sorted_by_price)

#checkpoint_12
"""
Add the new peppers pizza topping to our list pizza_and_prices.
"""
print("\ncheckpoint_12", before, pizza_and_prices_sorted_by_price)
pizza_and_prices.append([2.5, "peppers"])
#after we appended new item to the initial unsorted list of pizzas, we need to update the sorted list of pizzas based on the initial list
pizza_and_prices_sorted_by_price = sorted (
  pizza_and_prices,
  key=lambda x: (x[0],x[1])
)
#and we need to remember that earlier we sold all anchovis pizzas, hence we need to remove it as well.
pizza_and_prices_sorted_by_price.pop()
print(after, pizza_and_prices_sorted_by_price)

#checkpoint_13
"""
Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
"""
three_cheapest = pizza_and_prices_sorted_by_price[:3]
print("\ncheckpoint_13\nthree cheapest slices are: ", three_cheapest)