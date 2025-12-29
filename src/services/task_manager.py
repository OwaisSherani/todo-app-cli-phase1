"""
TaskManager service for managing todo tasks in memory with extended features.
"""
import sys
import os
from datetime import datetime, date
from typing import List, Optional, Dict, Any

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task
from src.services.recurrence_service import RecurrenceService
from src.services.reminder_service import ReminderService


class TaskManager:
    """
    Business logic layer for managing tasks with extended features.
    Maintains an in-memory collection of tasks and provides operations on them.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1
        self.recurrence_service = RecurrenceService()
        self.reminder_service = ReminderService()

    def add_task(self, title: str, description: str = "", priority: str = "Medium",
                 tags: List[str] = None, due_date=None, recurrence_pattern: str = None) -> Task:
        """
        Create a new task with the next available ID.

        Args:
            title: Required title of the task
            description: Optional description of the task
            priority: Priority level of the task (default: "Medium")
            tags: List of tags associated with the task (default: [])
            due_date: Due date of the task (default: None)
            recurrence_pattern: Recurrence pattern of the task (default: None)

        Returns:
            Task: The newly created task with assigned ID

        Raises:
            ValueError: If title is empty or invalid
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title must be a non-empty string")

        if not isinstance(description, str):
            raise ValueError("Task description must be a string")

        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Task priority must be one of: High, Medium, Low")

        if tags is None:
            tags = []
        if not isinstance(tags, list):
            raise ValueError("Task tags must be a list of strings")
        for tag in tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("Task tags must be non-empty strings")

        if due_date is not None and not isinstance(due_date, datetime):
            raise ValueError("Task due date must be a datetime object or None")

        if recurrence_pattern is not None and recurrence_pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Task recurrence pattern must be one of: daily, weekly, monthly")

        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence_pattern=recurrence_pattern
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Return all tasks in the collection.

        Returns:
            List[Task]: All tasks in the collection
        """
        return self.tasks.copy()  # Return a copy to prevent external modification

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Return a specific task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID, or None if not found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    priority: Optional[str] = None, tags: Optional[List[str]] = None,
                    due_date=None, recurrence_pattern: Optional[str] = None) -> Task:
        """
        Update an existing task's information.

        Args:
            task_id: The ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)
            priority: New priority for the task (optional)
            tags: New tags for the task (optional)
            due_date: New due date for the task (optional)
            recurrence_pattern: New recurrence pattern for the task (optional)

        Returns:
            Task: The updated task

        Raises:
            ValueError: If task doesn't exist or provided values are invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        # Update the task with provided values
        task.update(
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence_pattern=recurrence_pattern
        )

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the collection.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task didn't exist

        Raises:
            ValueError: If task ID is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def toggle_task_status(self, task_id: int) -> Task:
        """
        Toggle the completion status of a task.
        If the task is recurring and being marked as complete, create the next occurrence.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            Task: The task with toggled completion status

        Raises:
            ValueError: If task doesn't exist or task ID is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        if task.completed:
            task.mark_incomplete()
        else:
            task.mark_complete()

            # If this is a recurring task, create the next occurrence
            if task.recurrence_pattern:
                next_task = self.recurrence_service.create_next_occurrence(task)
                # Assign a new ID to the next occurrence
                next_task.id = self.next_id
                self.next_id += 1
                self.tasks.append(next_task)

        return task

    def set_task_priority(self, task_id: int, priority: str) -> Task:
        """
        Set the priority of a task.

        Args:
            task_id: The ID of the task to update
            priority: The new priority level

        Returns:
            Task: The updated task

        Raises:
            ValueError: If task doesn't exist or priority is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Task priority must be one of: High, Medium, Low")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task.update(priority=priority)
        return task

    def add_task_tags(self, task_id: int, tags: List[str]) -> Task:
        """
        Add tags to a task.

        Args:
            task_id: The ID of the task to update
            tags: List of tags to add

        Returns:
            Task: The updated task

        Raises:
            ValueError: If task doesn't exist or tags are invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(tags, list):
            raise ValueError("Task tags must be a list of strings")
        for tag in tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("Task tags must be non-empty strings")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        # Add new tags to existing tags, avoiding duplicates
        new_tags = [tag for tag in tags if tag not in task.tags]
        updated_tags = task.tags + new_tags
        task.update(tags=updated_tags)
        return task

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Return tasks matching the keyword in title or description.

        Args:
            keyword: The keyword to search for

        Returns:
            List[Task]: Tasks matching the keyword
        """
        if not isinstance(keyword, str):
            raise ValueError("Search keyword must be a string")

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, filters: Dict[str, Any]) -> List[Task]:
        """
        Return tasks matching the specified filters.

        Args:
            filters: Dictionary of filter criteria (status, priority, tags, due_date)

        Returns:
            List[Task]: Tasks matching the filter criteria
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters must be a dictionary")

        filtered_tasks = self.tasks.copy()

        # Filter by status
        if 'status' in filters:
            status = filters['status']
            if status == 'completed':
                filtered_tasks = [task for task in filtered_tasks if task.completed]
            elif status == 'pending':
                filtered_tasks = [task for task in filtered_tasks if not task.completed]
            else:
                raise ValueError("Status filter must be 'completed' or 'pending'")

        # Filter by priority
        if 'priority' in filters:
            priority = filters['priority']
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

        # Filter by tags
        if 'tags' in filters:
            tags = filters['tags']
            if isinstance(tags, str):
                tags = [tags]  # Convert single tag to list
            if isinstance(tags, list):
                # Find tasks that have all the specified tags
                for tag in tags:
                    filtered_tasks = [
                        task for task in filtered_tasks
                        if tag in task.tags
                    ]
            else:
                raise ValueError("Tags filter must be a string or list of strings")

        # Filter by due date
        if 'due_date' in filters:
            due_date = filters['due_date']
            filtered_tasks = [
                task for task in filtered_tasks
                if task.due_date and task.due_date.date() == due_date.date()
            ]

        return filtered_tasks

    def sort_tasks(self, sort_by: str, ascending: bool = True) -> List[Task]:
        """
        Return tasks sorted by the specified criteria.

        Args:
            sort_by: Criteria to sort by ('due_date', 'priority', 'title')
            ascending: Sort order (default: True for ascending)

        Returns:
            List[Task]: Tasks sorted by the specified criteria
        """
        if sort_by not in ['due_date', 'priority', 'title']:
            raise ValueError("Sort by must be 'due_date', 'priority', or 'title'")

        # Define priority order for sorting
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}

        if sort_by == 'due_date':
            # Sort by due date, with None values at the end
            sorted_tasks = sorted(
                self.tasks,
                key=lambda task: (task.due_date is None, task.due_date),
                reverse=not ascending
            )
        elif sort_by == 'priority':
            # Sort by priority using the defined order
            sorted_tasks = sorted(
                self.tasks,
                key=lambda task: priority_order[task.priority],
                reverse=not ascending
            )
        elif sort_by == 'title':
            # Sort by title alphabetically
            sorted_tasks = sorted(
                self.tasks,
                key=lambda task: task.title.lower(),
                reverse=not ascending
            )

        return sorted_tasks

    def set_task_recurrence(self, task_id: int, recurrence_pattern: str) -> Task:
        """
        Set the recurrence pattern for a task.

        Args:
            task_id: The ID of the task to update
            recurrence_pattern: The recurrence pattern

        Returns:
            Task: The updated task

        Raises:
            ValueError: If task doesn't exist or recurrence pattern is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if recurrence_pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Task recurrence pattern must be one of: daily, weekly, monthly")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task.update(recurrence_pattern=recurrence_pattern)
        return task

    def set_task_due_date(self, task_id: int, due_date) -> Task:
        """
        Set the due date for a task.

        Args:
            task_id: The ID of the task to update
            due_date: The due date

        Returns:
            Task: The updated task

        Raises:
            ValueError: If task doesn't exist or due date is invalid
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if due_date is not None and not isinstance(due_date, datetime):
            raise ValueError("Task due date must be a datetime object or None")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task.update(due_date=due_date)
        return task

    def get_overdue_tasks(self) -> List[Task]:
        """
        Return tasks that are past their due date and still pending.

        Returns:
            List[Task]: Overdue tasks
        """
        now = datetime.now()
        return [
            task for task in self.tasks
            if task.due_date and task.due_date < now and not task.completed
        ]

    def get_due_today_tasks(self) -> List[Task]:
        """
        Return tasks that are due today and still pending.

        Returns:
            List[Task]: Tasks due today
        """
        today = date.today()
        return [
            task for task in self.tasks
            if task.due_date and task.due_date.date() == today and not task.completed
        ]

    def get_due_soon_tasks(self) -> List[Task]:
        """
        Return tasks that are due in the next 7 days and still pending.

        Returns:
            List[Task]: Tasks due soon
        """
        from datetime import timedelta
        today = date.today()
        next_week = today + timedelta(days=7)
        return [
            task for task in self.tasks
            if task.due_date and today < task.due_date.date() <= next_week and not task.completed
        ]