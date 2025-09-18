task = input("Enter a task description: ")
priority = input("high, medium, low: ")
time_bound = input("Is the task is time-bound (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case _ :
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
