import csv

from src.deadlined_reminder import DeadlinedReminder

# import sys
# sys.path.append("c:\\Users\\xinmwu\\Documents\\GitHub\\python-build-cli-planner-app")

from src.reminder import PoliteReminder
from src.deadlined_reminder import DateReminder

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):
    
    if not issubclass(ReminderClass, DeadlinedReminder):
        raise TypeError('Invalid Reminder Class')
    
    reminder = ReminderClass(text, date)

    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)
