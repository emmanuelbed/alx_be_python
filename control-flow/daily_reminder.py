# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note:'{task}' is a {priority} priority task. Consider completing it very soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it very soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it very soon.")    
    
