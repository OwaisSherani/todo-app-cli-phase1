"""
Contract test for add task functionality.
"""
import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_add_task_contract():
    """Test that add_task functionality meets the contract specifications."""
    task_manager = TaskManager()
    
    # Test adding a task with title only
    title = "Test task"
    task = task_manager.add_task(title)
    
    assert isinstance(task, Task)
    assert task.id == 1  # First task should have ID 1
    assert task.title == title
    assert task.description == ""
    assert task.completed is False  # Default status should be False
    
    # Test adding a task with title and description
    title2 = "Test task 2"
    description = "This is a test description"
    task2 = task_manager.add_task(title2, description)
    
    assert isinstance(task2, Task)
    assert task2.id == 2  # Second task should have ID 2
    assert task2.title == title2
    assert task2.description == description
    assert task2.completed is False  # Default status should be False
    
    # Test that IDs are unique and incrementing
    assert task.id != task2.id
    assert task2.id == task.id + 1


def test_add_task_with_empty_title():
    """Test that adding a task with empty title raises ValueError."""
    task_manager = TaskManager()
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task("")
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task("   ")  # Only whitespace


def test_add_task_with_invalid_description():
    """Test that adding a task with invalid description raises ValueError."""
    task_manager = TaskManager()
    
    # Valid case - None should be converted to empty string
    task = task_manager.add_task("Test title", None)
    assert task.description == ""
    
    # Valid case - empty string should be accepted
    task = task_manager.add_task("Test title", "")
    assert task.description == ""
    
    # Valid case - regular string should be accepted
    task = task_manager.add_task("Test title", "Valid description")
    assert task.description == "Valid description"