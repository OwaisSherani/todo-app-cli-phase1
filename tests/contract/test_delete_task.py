"""
Contract test for delete task functionality.
"""
import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_delete_task_contract():
    """Test that delete task functionality meets the contract specifications."""
    task_manager = TaskManager()
    
    # Add a few tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3", "Description 3")
    
    # Verify all tasks exist
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 3
    
    # Delete one task
    result = task_manager.delete_task(task2.id)
    
    # Verify the deletion was successful
    assert result is True
    
    # Verify the task is no longer in the list
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 2
    
    # Verify the correct task was deleted
    task_ids = [task.id for task in all_tasks]
    assert task2.id not in task_ids
    assert task1.id in task_ids
    assert task3.id in task_ids


def test_delete_nonexistent_task():
    """Test that deleting a non-existent task returns False."""
    task_manager = TaskManager()
    
    # Add a task
    task = task_manager.add_task("Task 1", "Description 1")
    
    # Try to delete a non-existent task
    result = task_manager.delete_task(999)
    
    # Verify the result is False
    assert result is False
    
    # Verify the existing task is still there
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == task.id


def test_delete_task_invalid_id():
    """Test that deleting with invalid ID raises ValueError."""
    task_manager = TaskManager()
    
    # Add a task
    task_manager.add_task("Task 1", "Description 1")
    
    # Attempt to delete with invalid IDs
    invalid_ids = [0, -1, "invalid"]
    
    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.delete_task(invalid_id)


def test_delete_all_tasks():
    """Test deleting all tasks."""
    task_manager = TaskManager()
    
    # Add a few tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3", "Description 3")
    
    # Verify all tasks exist
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 3
    
    # Delete all tasks
    result1 = task_manager.delete_task(task1.id)
    result2 = task_manager.delete_task(task2.id)
    result3 = task_manager.delete_task(task3.id)
    
    # Verify all deletions were successful
    assert result1 is True
    assert result2 is True
    assert result3 is True
    
    # Verify no tasks remain
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 0


def test_delete_task_persistence():
    """Test that deleted tasks remain deleted."""
    task_manager = TaskManager()
    
    # Add a task
    task = task_manager.add_task("Task 1", "Description 1")
    
    # Verify the task exists
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    
    # Delete the task
    result = task_manager.delete_task(task.id)
    assert result is True
    
    # Verify the task is gone
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 0
    
    # Try to delete the same task again
    result = task_manager.delete_task(task.id)
    assert result is False