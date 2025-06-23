"""
We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.
"""

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade+10 for grade in grades]
print(scaled_grades)

numbers = [2, -1, 79, 33, -45]

no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

"""
We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
"""

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [h for h in heights if h>161 ]
print(can_ride_coaster )

# Your code below:

"""
Create a list called single_digits that consists of the numbers 0-9 (inclusive).
"""
single_digits = list(range(10))
print(single_digits)
"""
Create a for loop that goes through single_digits and prints out each one.
"""
for i in single_digits:
  print(i)

"""
Before the loop, create a list called squares. Assign it to be an empty list to begin with.
"""
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  print(squares)

"""
Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
"""

cubes = [n**3 for n in single_digits]
print(cubes)

