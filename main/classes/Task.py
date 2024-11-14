from datetime import *

class Task:
    def __init__(self, title, subject, description, due_date, priority):
        self.title = title
        self.subject = subject
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        self.priority = priority
        self.status = False

    def check_status(self):
        if not self.status:
            status = "Pending"
        else:
            status = "Completed"
        return status
    def is_due_today(self, current_date):
        return self.due_date == current_date

    def is_upcoming(self, current_date):
        return self.due_date > current_date

    def is_overdue(self, current_date):
        return self.due_date < current_date

    def days_remaining(self, current_date):
        if self.due_date > current_date:
            days = self.due_date - current_date
            return days.days

    def days_passed(self, current_date):
        if self.due_date < current_date:
            days = current_date - self.due_date
            return days.days