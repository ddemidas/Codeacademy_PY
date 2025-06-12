last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

#checkpoint_1
subjects = [
  "physics", 
  "calculus", 
  "poetry", 
  "history"
]

print(subjects)

#checkpoint_2
grades = [
  98, 
  97, 
  85, 
  88
]

print(grades)

#checkpoint_3
gradebook = [
  ["physics", 98], 
  ["calculus", 97], 
  ["poetry", 85], 
  ["history", 88] 
]

#checkpoint_4
print(gradebook)

#checkpoint_5
gradebook.append(["computer science", 100])
print("====checkpoint_5====")
print(gradebook)
#checkpoint_6
gradebook.append(["visual arts", 93])
print("====checkpoint_6====")
print(gradebook)

#checkpoint_7
print("====checkpoint_7====")
gradebook[5][1]=100
print(gradebook)

#checkpoint_8
print("====checkpoint_8====")
print(gradebook)
#print(gradebook[2])
#print(gradebook[2][1])
gradebook[2].remove(85)
print(gradebook)

#checkpoint_9
print("====checkpoint_9====")
print(gradebook)
gradebook[2].append("Pass")
print(gradebook)

#checkpoint_10
print("====checkpoint_10====")
print("last_semester_gradebook:")
print(last_semester_gradebook)
print("gradebook:")
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print("full_gradebook:")
print(full_gradebook)