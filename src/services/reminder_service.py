"""
ReminderService for handling due dates and reminders.
"""
import sys
import os
from datetime import datetime, date, timedelta
from typing import List

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task


class ReminderService:
    """
    Service for tracking due dates and providing reminder notifications.
    """
    
    def __init__(self):
        """Initialize the ReminderService."""
        pass

    def get_overdue_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        Get tasks that are past their due date and still pending.

        Args:
            tasks: List of tasks to check

        Returns:
            List[Task]: Overdue tasks
        """
        now = datetime.now()
        return [
            task for task in tasks 
            if task.due_date and task.due_date < now and not task.completed
        ]

    def get_due_today_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        Get tasks that are due today and still pending.

        Args:
            tasks: List of tasks to check

        Returns:
            List[Task]: Tasks due today
        """
        today = date.today()
        return [
            task for task in tasks 
            if task.due_date and task.due_date.date() == today and not task.completed
        ]

    def get_due_soon_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        Get tasks that are due in the next 7 days and still pending.

        Args:
            tasks: List of tasks to check

        Returns:
            List[Task]: Tasks due soon
        """
        today = date.today()
        next_week = today + timedelta(days=7)
        return [
            task for task in tasks 
            if task.due_date and today < task.due_date.date() <= next_week and not task.completed
        ]

    def get_upcoming_reminders(self, tasks: List[Task]) -> dict:
        """
        Get all upcoming reminders grouped by type.

        Args:
            tasks: List of tasks to check

        Returns:
            dict: Dictionary with keys 'overdue', 'due_today', 'due_soon' containing respective tasks
        """
        return {
            'overdue': self.get_overdue_tasks(tasks),
            'due_today': self.get_due_today_tasks(tasks),
            'due_soon': self.get_due_soon_tasks(tasks)
        }

    def generate_reminder_message(self, task: Task) -> str:
        """
        Generate a reminder message for a task.

        Args:
            task: The task to generate a reminder for

        Returns:
            str: Reminder message
        """
        if not task.due_date:
            return f"Task '{task.title}' has no due date."

        due_date_str = task.due_date.strftime("%Y-%m-%d")
        days_until_due = (task.due_date.date() - date.today()).days

        if days_until_due < 0:
            return f"OVERDUE: Task '{task.title}' was due on {due_date_str} ({abs(days_until_due)} days ago)."
        elif days_until_due == 0:
            return f"DUE TODAY: Task '{task.title}' is due today ({due_date_str})."
        elif days_until_due == 1:
            return f"DUE TOMORROW: Task '{task.title}' is due tomorrow ({due_date_str})."
        else:
            return f"DUE SOON: Task '{task.title}' is due in {days_until_due} days ({due_date_str})."