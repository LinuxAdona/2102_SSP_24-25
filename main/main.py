from classes.Task import *

task1 = Task("Activity 1", "ACP", 'Hays', '2024-11-20', 1)

if task1.is_due_today(date.today()):
    print("Due Today:", task1)
elif task1.is_upcoming(date.today()):
    print("Upcoming:", task1.days_remaining(date.today()), "Days", task1.__str__())
elif task1.is_overdue(date.today()):
    print("Overdue:", task1.days_passed(date.today()), "Days", task1.__str__())
else:
    print("Not Due:", task1)