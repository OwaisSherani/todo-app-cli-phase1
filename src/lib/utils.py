"""
Utility functions for the Todo CLI Application.
"""
import re
from datetime import datetime
from typing import Any, Dict, List, Union


def validate_priority(priority: str) -> bool:
    """
    Validate that the priority is one of the allowed values.
    
    Args:
        priority: The priority level to validate
        
    Returns:
        bool: True if the priority is valid, False otherwise
    """
    return priority in ["High", "Medium", "Low"]


def validate_tags(tags: List[str]) -> bool:
    """
    Validate that the tags are a list of non-empty strings.
    
    Args:
        tags: The list of tags to validate
        
    Returns:
        bool: True if the tags are valid, False otherwise
    """
    if not isinstance(tags, list):
        return False
    
    for tag in tags:
        if not isinstance(tag, str) or not tag.strip():
            return False
    
    return True


def validate_date(date_str: str) -> bool:
    """
    Validate that the date string is in YYYY-MM-DD format.
    
    Args:
        date_str: The date string to validate
        
    Returns:
        bool: True if the date string is valid, False otherwise
    """
    if not isinstance(date_str, str):
        return False
    
    # Check if the date string matches YYYY-MM-DD format
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        return False
    
    try:
        # Try to parse the date to ensure it's a valid date
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_recurrence_pattern(pattern: str) -> bool:
    """
    Validate that the recurrence pattern is one of the allowed values.
    
    Args:
        pattern: The recurrence pattern to validate
        
    Returns:
        bool: True if the pattern is valid, False otherwise
    """
    return pattern in ["daily", "weekly", "monthly"]


def format_task_display(task: Any) -> str:
    """
    Format a task for display in the CLI.
    
    Args:
        task: The task object to format
        
    Returns:
        str: Formatted string representation of the task
    """
    status = "Completed" if task.completed else "Pending"
    priority = getattr(task, 'priority', 'Medium')
    tags = getattr(task, 'tags', [])
    due_date = getattr(task, 'due_date', None)
    
    result = f"ID: {task.id} | {status} | Priority: {priority} | {task.title}"
    
    if tags:
        result += f" | Tags: {', '.join(tags)}"
    
    if due_date:
        result += f" | Due: {due_date}"
    
    if task.description:
        result += f"\n  Description: {task.description}"
    
    return result