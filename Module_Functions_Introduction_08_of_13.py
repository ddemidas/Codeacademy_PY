# Write your code below:
#checkpoint1
"""
Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.
"""
#checkpoint2
"""
First, we want to introduce the trip to users. Use print() in our function to output Here is what your trip will look like!.
"""
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ" ):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + str(first_destination) + " then " + str(second_destination) + ", and lastly " + str(final_destination))
trip_planner("London", "India", "New Zealand")
print("\n")
trip_planner("France", "Germany", "Denmark")
print("\n")
trip_planner("Denmark", "France", "Germany")
print("\n")
trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany")
print("\n")
trip_planner("Brooklyn", "Queens")