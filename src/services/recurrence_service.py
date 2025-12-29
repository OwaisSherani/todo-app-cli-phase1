"""
RecurrenceService for handling recurring tasks.
"""
import sys
import os
from datetime import datetime, timedelta
from typing import List

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task


class RecurrenceService:
    """
    Service for handling recurring task scheduling and creation.
    """
    
    def __init__(self):
        """Initialize the RecurrenceService."""
        pass

    def create_next_occurrence(self, task: Task) -> Task:
        """
        Create the next occurrence of a recurring task based on its recurrence pattern.

        Args:
            task: The completed recurring task

        Returns:
            Task: A new task instance with updated due date based on recurrence pattern
        """
        if not task.recurrence_pattern:
            raise ValueError("Task must have a recurrence pattern to create next occurrence")

        # Calculate the next due date based on the recurrence pattern
        next_due_date = self._calculate_next_due_date(task.due_date, task.recurrence_pattern)

        # Create a new task with the same properties but updated due date
        new_task = Task(
            id=task.id,  # This will be updated by the TaskManager
            title=task.title,
            description=task.description,
            completed=False,  # New occurrence is not completed
            priority=task.priority,
            tags=task.tags.copy(),  # Copy the tags
            due_date=next_due_date,
            recurrence_pattern=task.recurrence_pattern
        )

        return new_task

    def _calculate_next_due_date(self, current_due_date: datetime, pattern: str) -> datetime:
        """
        Calculate the next due date based on the current due date and recurrence pattern.

        Args:
            current_due_date: The current due date
            pattern: The recurrence pattern ('daily', 'weekly', 'monthly')

        Returns:
            datetime: The next due date
        """
        if not current_due_date:
            # If no current due date, use today as the starting point
            current_due_date = datetime.now()

        if pattern == 'daily':
            return current_due_date + timedelta(days=1)
        elif pattern == 'weekly':
            return current_due_date + timedelta(weeks=1)
        elif pattern == 'monthly':
            # For monthly recurrence, we need to handle month boundaries
            current_month = current_due_date.month
            current_year = current_due_date.year
            
            # Calculate next month
            if current_month == 12:
                next_month = 1
                next_year = current_year + 1
            else:
                next_month = current_month + 1
                next_year = current_year
            
            # Handle day overflow (e.g., Jan 31 -> Feb 31 doesn't exist)
            current_day = current_due_date.day
            max_day_next_month = self._days_in_month(next_year, next_month)
            next_day = min(current_day, max_day_next_month)
            
            return current_due_date.replace(year=next_year, month=next_month, day=next_day)
        else:
            raise ValueError(f"Invalid recurrence pattern: {pattern}")

    def _days_in_month(self, year: int, month: int) -> int:
        """
        Calculate the number of days in a given month.

        Args:
            year: The year
            month: The month (1-12)

        Returns:
            int: Number of days in the month
        """
        # Days in each month (index 0 = Jan, index 11 = Dec)
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Adjust for leap years
        if month == 2 and self._is_leap_year(year):
            return 29
        else:
            return days_per_month[month - 1]

    def _is_leap_year(self, year: int) -> bool:
        """
        Check if a year is a leap year.

        Args:
            year: The year to check

        Returns:
            bool: True if leap year, False otherwise
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)