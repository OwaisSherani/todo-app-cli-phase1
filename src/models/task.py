"""
Task model representing a single todo item with extended properties.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo item with properties: ID, Title, Description, Status,
    Priority, Tags, Due Date, and Recurrence Pattern.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Required title of the task
        description (str): Optional description of the task
        completed (bool): Completion status of the task (default: False)
        priority (str): Priority level of the task (default: "Medium")
        tags (List[str]): List of tags associated with the task (default: [])
        due_date (Optional[datetime]): Due date of the task (default: None)
        recurrence_pattern (Optional[str]): Recurrence pattern of the task (default: None)
        created_at (datetime): Creation timestamp of the task (default: current time)
        completed_at (Optional[datetime]): Completion timestamp of the task (default: None)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "Medium"
    tags: List[str] = field(default_factory=list)
    due_date: Optional[datetime] = None
    recurrence_pattern: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Task title must be a non-empty string")

        if not isinstance(self.description, str):
            raise ValueError("Task description must be a string")

        if not isinstance(self.completed, bool):
            raise ValueError("Task completion status must be a boolean")

        if self.priority not in ["High", "Medium", "Low"]:
            raise ValueError("Task priority must be one of: High, Medium, Low")

        if not isinstance(self.tags, list):
            raise ValueError("Task tags must be a list of strings")
        for tag in self.tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("Task tags must be non-empty strings")

        if self.due_date is not None and not isinstance(self.due_date, datetime):
            raise ValueError("Task due date must be a datetime object or None")

        if self.recurrence_pattern is not None and self.recurrence_pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Task recurrence pattern must be one of: daily, weekly, monthly")

        if not isinstance(self.created_at, datetime):
            raise ValueError("Task created_at must be a datetime object")

        if self.completed_at is not None and not isinstance(self.completed_at, datetime):
            raise ValueError("Task completed_at must be a datetime object or None")

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True
        self.completed_at = datetime.now()

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None

    def update(self, title: Optional[str] = None, description: Optional[str] = None,
               priority: Optional[str] = None, tags: Optional[List[str]] = None,
               due_date: Optional[datetime] = None, recurrence_pattern: Optional[str] = None):
        """
        Update the task with new information.

        Args:
            title: New title for the task (optional)
            description: New description for the task (optional)
            priority: New priority for the task (optional)
            tags: New tags for the task (optional)
            due_date: New due date for the task (optional)
            recurrence_pattern: New recurrence pattern for the task (optional)
        """
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Task title must be a non-empty string")
            self.title = title

        if description is not None:
            if not isinstance(description, str):
                raise ValueError("Task description must be a string")
            self.description = description

        if priority is not None:
            if priority not in ["High", "Medium", "Low"]:
                raise ValueError("Task priority must be one of: High, Medium, Low")
            self.priority = priority

        if tags is not None:
            if not isinstance(tags, list):
                raise ValueError("Task tags must be a list of strings")
            for tag in tags:
                if not isinstance(tag, str) or not tag.strip():
                    raise ValueError("Task tags must be non-empty strings")
            self.tags = tags

        if due_date is not None:
            if not isinstance(due_date, datetime):
                raise ValueError("Task due date must be a datetime object")
            self.due_date = due_date

        if recurrence_pattern is not None:
            if recurrence_pattern not in ["daily", "weekly", "monthly"]:
                raise ValueError("Task recurrence pattern must be one of: daily, weekly, monthly")
            self.recurrence_pattern = recurrence_pattern