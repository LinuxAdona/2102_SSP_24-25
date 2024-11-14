from classes.Task import *

task1 = Task("Activity 1", "ACP", '2024-11-20', 1)

if task1.check_date(date.today()) == 0:
    print("today")
elif task1.check_date(date.today()) == -1:
    print("missed")
else:
    print("Days Remaining:", task1.check_date(date.today()))