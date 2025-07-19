# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match time_bound:
    case "yes":
        if priority == "high":
            print(f"'{task}' is a {priority} priority taskpriority task that requires immediate attention today!")
        elif priority == "medium":
            print(f"'{task}' is a {priority} priority task. Consider completing it very soon.")
        elif priority == "low":
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Incorrect Priority level")
    case "no":
        if priority == "high":
            print(f"'{task}' is a {priority} priority taskpriority task that requires immediate attention today!")
        elif priority == "medium":
            print(f"'{task}' is a {priority} priority task. Consider completing it very soon.")
        elif priority == "low":
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Incorrect Priority level")
    
