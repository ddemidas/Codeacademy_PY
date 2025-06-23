dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

print("=========\nThis is the end of this algorithm")

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i<21:
    continue
  print(i)