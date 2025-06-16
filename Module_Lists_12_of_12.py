inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#checkpoint_1
print("\ncheckpoint_1\n")
inventory_len = len(inventory)
print("This is how many items there are in the Jiho\'s shop: \n ")
print(inventory_len)

#checkpoint_2
print("\ncheckpoint_2\n")
first = inventory[0]
print("The firts element of the list is:\n ")
print(first)

#checkpoint_3
print("\ncheckpoint_3\n")
last = inventory[-1]
print("The last element of the list is:\n ")
print(last)

#checkpoint_4
print("\ncheckpoint_4\n")
inventory_2_6 = inventory[2:6]
print("The items starting from index 2 to but not index 6 are:\n ")
print(inventory_2_6)

#checkpoint_5
print("\ncheckpoint_5\n")
first_3 = inventory[:3]
print("First 3 items of the list are: \n")
print(first_3)

#checkpoint_6
print("\ncheckpoint_6\n")
twin_beds = inventory.count("twin bed")
print("This list contains this amount of twin beds: \n")
print(twin_beds)

#checkpoint_7
print("\ncheckpoint_7\n")
removed_item = inventory.pop(4)
print("This value has been removed from the list: \n")
print(removed_item)

#checkbox_8
print("\ncheckbox_8\n")
print("Before we add a new item the list looks like below: \n")
print(inventory)
print("After we add a new element 19th Century Bed Frame to the 11th position: \n")
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

#checkbox_9
print("\ncheckbox_9\n")
print("Before we sort: \n")
print(inventory)
inventory.sort()
print("After we sort: \n")
print(inventory)
