#prompt the user to give you a task description
task = input("Enter your task:")
# prompt the user for the priority level of the task
priority = input("Priority (high/medium/low):")
#ask if its time bound or not
time_bound = input("Is it time-bound? (yes/no):")

#check the answers
if priority not in ["high","medium","low"]:
    print("Invalid priority level. Please choose between 'high', 'medium', 'low'")
elif time_bound not in ['yes','no']:
    print("Invalid response.Please enter 'yes','no'")
else:
    #process the task based on the priority and time sensitivity
    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention!"
        case 'medium':
            reminder = f"Reminder: '{task}' is a medium priority task. Try to complete it soon."
        case 'low':
            reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
        
    #edit the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder += " Don't forget, it needs to be done today!"

        #print the reminder
        print("Reminder:",reminder)