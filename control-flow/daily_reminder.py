#prompt the user to give you a task description
Task = input("What is the task please?")
# prompt the user for the priority level of the task
Priority = input("What is the priority level of this task please?")
#ask if its time bound or not
Time_Bound = input("is it time bound? Please respond with yes/no")

#check the answers
if Priority not in ["high","medium","low"]:
    print("Invalid priority level. Please choose between 'high', 'medium', 'low'")
elif Time_Bound not in ['yes','no']:
    print("Invalid response.Please enter 'yes','no'")
else:
    #process the task based on the priority and time sensitivity
    match Priority:
        case 'high':
            reminder = f"Reminder: '{Task}' is a high priority task that requires immediate attention!"
        case 'medium':
            reminder = f"Reminder: '{Task}' is a medium priority task. Try to complete it soon."
        case 'low':
            reminder = f"Reminder: '{Task}' is a low priority task. Consider completing it when you have free time."
        
    #edit the reminder if the task is time-bound
    if Time_Bound == 'yes':
        reminder += " Don't forget, it needs to be done today!"

        #print the reminder
        print(reminder)