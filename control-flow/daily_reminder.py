# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority handling
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Adjust based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Simple loop to emphasize the reminder (prints 1 time here but could repeat if you want)
for _ in range(1):
    print("\nReminder:", reminder)

