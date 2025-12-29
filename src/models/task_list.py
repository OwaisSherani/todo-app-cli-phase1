"""
TaskList model representing a collection of tasks with search, filter, and sort capabilities.
"""
from datetime import datetime
from typing import List, Dict, Optional, Any
from src.models.task import Task


class TaskList:
    """
    Represents a collection of Task objects with enhanced functionality.
    """
    
    def __init__(self):
        """Initialize an empty task list."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "", priority: str = "Medium", 
                 tags: List[str] = None, due_date: datetime = None, 
                 recurrence_pattern: str = None) -> Task:
        """
        Add a new task to the list.

        Args:
            title: Required title of the task
            description: Optional description of the task
            priority: Priority level of the task (default: "Medium")
            tags: List of tags associated with the task (default: [])
            due_date: Due date of the task (default: None)
            recurrence_pattern: Recurrence pattern of the task (default: None)

        Returns:
            Task: The newly created task with assigned ID
        """
        if tags is None:
            tags = []
            
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
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

    def update_task(self, task_id: int, **kwargs) -> Task:
        """
        Update an existing task's properties.

        Args:
            task_id: The ID of the task to update
            **kwargs: Properties to update (title, description, priority, tags, due_date, recurrence_pattern)

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
        task.update(**kwargs)

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the collection.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task didn't exist
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> Task:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            Task: The task with updated completion status
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task.mark_complete()
        return task

    def mark_task_incomplete(self, task_id: int) -> Task:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            Task: The task with updated completion status
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")

        task.mark_incomplete()
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

    def get_recurring_tasks(self) -> List[Task]:
        """
        Return all tasks with recurrence patterns.

        Returns:
            List[Task]: Tasks with recurrence patterns
        """
        return [task for task in self.tasks if task.recurrence_pattern is not None]

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