"""
Contract test for toggle task status functionality.
"""
import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_toggle_task_status_contract():
    """Test that toggle task status functionality meets the contract specifications."""
    task_manager = TaskManager()
    
    # Add a task (default status is False/pending)
    task = task_manager.add_task("Test Task", "Test Description")
    
    # Verify initial state
    assert task.completed is False
    
    # Toggle the status (should become True/completed)
    toggled_task = task_manager.toggle_task_status(task.id)
    
    # Verify the status was toggled
    assert toggled_task.id == task.id
    assert toggled_task.completed is True
    
    # Toggle again (should become False/pending)
    toggled_task2 = task_manager.toggle_task_status(task.id)
    
    # Verify the status was toggled back
    assert toggled_task2.id == task.id
    assert toggled_task2.completed is False


def test_toggle_task_status_persistence():
    """Test that toggling status is persistent in the manager."""
    task_manager = TaskManager()
    
    # Add a task
    task = task_manager.add_task("Test Task", "Test Description")
    
    # Verify initial state
    retrieved_task = task_manager.get_task_by_id(task.id)
    assert retrieved_task.completed is False
    
    # Toggle the status
    task_manager.toggle_task_status(task.id)
    
    # Verify the change is persistent
    retrieved_task = task_manager.get_task_by_id(task.id)
    assert retrieved_task.completed is True
    
    # Toggle again
    task_manager.toggle_task_status(task.id)
    
    # Verify the change is persistent
    retrieved_task = task_manager.get_task_by_id(task.id)
    assert retrieved_task.completed is False


def test_toggle_nonexistent_task():
    """Test that toggling status of a non-existent task raises ValueError."""
    task_manager = TaskManager()
    
    # Add a task
    task = task_manager.add_task("Existing Task", "Description")
    
    # Try to toggle a non-existent task
    with pytest.raises(ValueError, match="Task with ID 999 does not exist"):
        task_manager.toggle_task_status(999)


def test_toggle_task_invalid_id():
    """Test that toggling with invalid ID raises ValueError."""
    task_manager = TaskManager()
    
    # Add a task
    task_manager.add_task("Existing Task", "Description")
    
    # Attempt to toggle with invalid IDs
    invalid_ids = [0, -1, "invalid"]
    
    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.toggle_task_status(invalid_id)


def test_toggle_multiple_tasks():
    """Test toggling status of multiple tasks."""
    task_manager = TaskManager()
    
    # Add multiple tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3", "Description 3")
    
    # Verify all tasks are initially pending
    assert task_manager.get_task_by_id(task1.id).completed is False
    assert task_manager.get_task_by_id(task2.id).completed is False
    assert task_manager.get_task_by_id(task3.id).completed is False
    
    # Toggle task1 to completed
    task_manager.toggle_task_status(task1.id)
    
    # Verify only task1 is completed
    assert task_manager.get_task_by_id(task1.id).completed is True
    assert task_manager.get_task_by_id(task2.id).completed is False
    assert task_manager.get_task_by_id(task3.id).completed is False
    
    # Toggle task2 to completed
    task_manager.toggle_task_status(task2.id)
    
    # Verify task1 and task2 are completed, task3 is pending
    assert task_manager.get_task_by_id(task1.id).completed is True
    assert task_manager.get_task_by_id(task2.id).completed is True
    assert task_manager.get_task_by_id(task3.id).completed is False
    
    # Toggle task1 back to pending
    task_manager.toggle_task_status(task1.id)
    
    # Verify task1 is pending, task2 is completed, task3 is pending
    assert task_manager.get_task_by_id(task1.id).completed is False
    assert task_manager.get_task_by_id(task2.id).completed is True
    assert task_manager.get_task_by_id(task3.id).completed is False