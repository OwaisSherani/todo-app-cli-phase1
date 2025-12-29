"""
Contract test for update task functionality.
"""
import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_update_task_contract():
    """Test that update task functionality meets the contract specifications."""
    task_manager = TaskManager()
    
    # Add a task to update
    original_title = "Original Title"
    original_description = "Original Description"
    task = task_manager.add_task(original_title, original_description)
    
    # Verify the task was created with correct properties
    assert task.title == original_title
    assert task.description == original_description
    assert task.completed is False
    
    # Update the task
    new_title = "Updated Title"
    new_description = "Updated Description"
    updated_task = task_manager.update_task(task.id, new_title, new_description)
    
    # Verify the task was updated correctly
    assert updated_task.id == task.id  # ID should remain the same
    assert updated_task.title == new_title
    assert updated_task.description == new_description
    assert updated_task.completed is False  # Status should remain unchanged
    
    # Verify the update is persistent in the manager
    retrieved_task = task_manager.get_task_by_id(task.id)
    assert retrieved_task.title == new_title
    assert retrieved_task.description == new_description


def test_update_task_partial():
    """Test updating only title or only description."""
    task_manager = TaskManager()
    
    # Add a task to update
    original_title = "Original Title"
    original_description = "Original Description"
    task = task_manager.add_task(original_title, original_description)
    
    # Update only the title
    new_title = "Updated Title"
    updated_task = task_manager.update_task(task.id, title=new_title)
    
    # Verify only title was updated
    assert updated_task.title == new_title
    assert updated_task.description == original_description  # Should remain unchanged
    assert updated_task.id == task.id
    
    # Update only the description
    new_description = "Updated Description"
    updated_task2 = task_manager.update_task(task.id, description=new_description)
    
    # Verify only description was updated
    assert updated_task2.title == new_title  # Should remain the updated title
    assert updated_task2.description == new_description
    assert updated_task2.id == task.id


def test_update_task_nonexistent():
    """Test that updating a non-existent task raises ValueError."""
    task_manager = TaskManager()
    
    # Attempt to update a task that doesn't exist
    with pytest.raises(ValueError, match="Task with ID 999 does not exist"):
        task_manager.update_task(999, "New Title", "New Description")


def test_update_task_invalid_id():
    """Test that updating with invalid ID raises ValueError."""
    task_manager = TaskManager()
    
    # Attempt to update with invalid IDs
    invalid_ids = [0, -1, "invalid"]
    
    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.update_task(invalid_id, "New Title", "New Description")


def test_update_task_empty_title():
    """Test that updating with empty title raises ValueError."""
    task_manager = TaskManager()
    
    # Add a task to update
    task = task_manager.add_task("Original Title")
    
    # Attempt to update with empty title
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.update_task(task.id, title="")
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.update_task(task.id, title="   ")  # Only whitespace