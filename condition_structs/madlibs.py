# Mad Libs Game

# 1. Get inputs
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")

# 2. Story template
story = f"One day, a {adjective} {animal} decided to {verb} over a {noun}."

# 3. Conditional twist
if adjective.lower() == "scary":
    story += " Everyone ran away in fear!"
else:
    story += " Everyone laughed happily."

# 4. Show story
print("\nHere is your Mad Libs story:")
print(story)
