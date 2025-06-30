hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

normal_price=0
for p in range(len(prices)):
  normal_price = prices[p]
  print("normal_price is: ", normal_price)

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#checkpoint1
"""
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.
"""

total_price = 0
print("\n")

#checkpoint2
"""
Loop through the prices list and add each price to the variable total_price.
"""
for i in range(len(prices)):
  total_price +=  prices[i]
  print("total_price is: ", str(total_price))

#checkpoint2
"""
After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.
"""

average_price = (total_price)/(len(prices))
#checkpoint4
"""
Print the value of average_price so the output looks like:
"""
print("\nAverage Haircut Price: ", str(average_price))

print("\n")
#checkpoint5
"""
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
"""
new_prices = []
reduced_prices = 0
for j in range(len(prices)):
  reduced_prices = (prices[j]-5)
  new_prices.append(reduced_prices)
  #print("reduced_price is: ", str(reduced_prices))

#checkpoint6
"""
Print new_prices
"""
print("The new lower prices are: ", str(new_prices))

#checkpoint7, #checkpoint8, #checkpoint9
"""
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.

Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!

Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
"""
print("\n")
total_revenue = 0
total_revenue_per_week_per_haircut = []
for i in range(len(prices)):
  total_revenue=prices[i]*last_week[i]
  total_revenue_per_week_per_haircut.append(total_revenue)
  #print("total_revenue per haircut is: ", total_revenue)
  
print("\nTotal revenue per week per haircut is: ", total_revenue_per_week_per_haircut)
total_revenue_ALL = sum(total_revenue_per_week_per_haircut)
#checkpoint10
"""
After your loop, print the value of total_revenue
"""
print("\nTotal revenue per week for all haircuts is: ", total_revenue_ALL)

#checkpoint11
"""
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.
"""
#average_daily_revenue = 0
average_daily_revenue = ((total_revenue_ALL)/7)
#here the owner can lose some money in average daily revenue up to 99 cents
#===
average_daily_revenue=int(average_daily_revenue)
#===
print("\nAverage daily revenue is: ", str(average_daily_revenue))

#checkpoint12
"""
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range(len(new_prices)) in your list comprehension to make i go from 0 to the last index of new_prices.
"""

cuts_under_30 = []
for i in range(len(new_prices)):
  if (new_prices[i]<30):
    cuts_under_30.append(hairstyles[i])

print("The haircuts cheaper than 30 are: \n", str(cuts_under_30), "\nWelcome!")
