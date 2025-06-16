games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
before = "before:\n"
after = "after:\n"

# Your code below:
#checkpoint_1
print(before, games)
games_sorted = sorted(games)
print(after + "untouched list\n", games)
print(after + "new list\n", games_sorted)

#checkpoint_2
print("I have to print lists again without any concatenation, becuase the interpreter wants me to do so in order to continue the task:\n")

print(games)
print(games_sorted)