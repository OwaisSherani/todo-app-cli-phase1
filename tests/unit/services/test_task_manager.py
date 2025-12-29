"""
Unit tests for the TaskManager service, specifically for add_task method.
"""
import pytest
from src.services.task_manager import TaskManager
from src.models.task import Task


def test_add_task_basic():
    """Test basic functionality of add_task method."""
    task_manager = TaskManager()
    
    title = "Test Task"
    description = "Test Description"
    
    task = task_manager.add_task(title, description)
    
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == title
    assert task.description == description
    assert task.completed is False


def test_add_task_without_description():
    """Test add_task method when no description is provided."""
    task_manager = TaskManager()
    
    title = "Test Task"
    
    task = task_manager.add_task(title)
    
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == title
    assert task.description == ""
    assert task.completed is False


def test_add_multiple_tasks():
    """Test adding multiple tasks and verifying unique IDs."""
    task_manager = TaskManager()
    
    task1 = task_manager.add_task("Task 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3")
    
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3
    
    assert task1.title == "Task 1"
    assert task2.title == "Task 2"
    assert task3.title == "Task 3"
    
    assert task2.description == "Description 2"


def test_add_task_empty_title_error():
    """Test that add_task raises ValueError when title is empty."""
    task_manager = TaskManager()
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task("")
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task("   ")  # Only whitespace


def test_add_task_invalid_title_type():
    """Test that add_task raises ValueError when title is not a string."""
    task_manager = TaskManager()
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task(123)
    
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.add_task(None)


def test_add_task_invalid_description_type():
    """Test that add_task raises ValueError when description is not a string."""
    task_manager = TaskManager()
    
    with pytest.raises(ValueError, match="Task description must be a string"):
        task_manager.add_task("Valid Title", 123)


def test_add_task_id_generation():
    """Test that task IDs are generated correctly."""
    task_manager = TaskManager()
    
    # Add several tasks and verify IDs are sequential
    for i in range(1, 6):
        task = task_manager.add_task(f"Task {i}")
        assert task.id == i


def test_add_task_persistence():
    """Test that added tasks are stored in the manager."""
    task_manager = TaskManager()

    task = task_manager.add_task("Persistent Task", "Should be stored")

    # Verify the task is in the manager's list
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == task.id
    assert all_tasks[0].title == task.title
    assert all_tasks[0].description == task.description


def test_get_all_tasks_empty():
    """Test get_all_tasks when no tasks exist."""
    task_manager = TaskManager()

    tasks = task_manager.get_all_tasks()

    assert tasks == []
    assert len(tasks) == 0


def test_get_all_tasks_with_tasks():
    """Test get_all_tasks when tasks exist."""
    task_manager = TaskManager()

    # Add several tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3")

    tasks = task_manager.get_all_tasks()

    # Verify all tasks are returned
    assert len(tasks) == 3
    assert tasks[0].id == task1.id
    assert tasks[1].id == task2.id
    assert tasks[2].id == task3.id

    # Verify properties are preserved
    assert tasks[0].title == "Task 1"
    assert tasks[0].description == "Description 1"
    assert tasks[0].completed is False

    assert tasks[1].title == "Task 2"
    assert tasks[1].description == "Description 2"
    assert tasks[1].completed is False

    assert tasks[2].title == "Task 3"
    assert tasks[2].description == ""
    assert tasks[2].completed is False


def test_get_all_tasks_returns_copy():
    """Test that get_all_tasks returns a copy of the internal list."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task("Task 1")

    # Get the list
    tasks = task_manager.get_all_tasks()

    # Verify it's a copy by modifying it
    original_length = len(tasks)
    if tasks:
        tasks.pop()  # Remove an item from the returned list

    # Internal list should be unchanged
    internal_tasks = task_manager.get_all_tasks()
    assert len(internal_tasks) == original_length


def test_update_task_full():
    """Test updating a task with new title and description."""
    task_manager = TaskManager()

    # Add a task
    original_task = task_manager.add_task("Original Title", "Original Description")

    # Update the task
    new_title = "New Title"
    new_description = "New Description"
    updated_task = task_manager.update_task(original_task.id, new_title, new_description)

    # Verify the task was updated
    assert updated_task.id == original_task.id
    assert updated_task.title == new_title
    assert updated_task.description == new_description
    assert updated_task.completed is False  # Status should remain unchanged


def test_update_task_partial():
    """Test updating only title or only description."""
    task_manager = TaskManager()

    # Add a task
    original_task = task_manager.add_task("Original Title", "Original Description")

    # Update only the title
    new_title = "New Title"
    updated_task = task_manager.update_task(original_task.id, title=new_title)

    # Verify only title was updated
    assert updated_task.title == new_title
    assert updated_task.description == "Original Description"  # Should remain unchanged

    # Update only the description
    new_description = "New Description"
    updated_task2 = task_manager.update_task(original_task.id, description=new_description)

    # Verify only description was updated
    assert updated_task2.title == new_title  # Should remain the updated title
    assert updated_task2.description == new_description


def test_update_task_nonexistent():
    """Test that updating a non-existent task returns False."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task("Existing Task")

    # Attempt to update a non-existent task
    with pytest.raises(ValueError, match="Task with ID 999 does not exist"):
        task_manager.update_task(999, "New Title", "New Description")


def test_update_task_invalid_id():
    """Test that updating with invalid ID raises ValueError."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task("Existing Task")

    # Attempt to update with invalid IDs
    invalid_ids = [0, -1]

    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.update_task(invalid_id, "New Title", "New Description")


def test_update_task_empty_title():
    """Test that updating with empty title raises ValueError."""
    task_manager = TaskManager()

    # Add a task
    task = task_manager.add_task("Original Title")

    # Attempt to update with empty title
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.update_task(task.id, title="")

    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task_manager.update_task(task.id, title="   ")  # Only whitespace


def test_delete_task_success():
    """Test successfully deleting a task."""
    task_manager = TaskManager()

    # Add a task
    task = task_manager.add_task("Task to Delete", "Description")

    # Verify the task exists
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == task.id

    # Delete the task
    result = task_manager.delete_task(task.id)

    # Verify the deletion was successful
    assert result is True

    # Verify the task is gone
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 0


def test_delete_task_nonexistent():
    """Test deleting a non-existent task."""
    task_manager = TaskManager()

    # Add a task
    existing_task = task_manager.add_task("Existing Task", "Description")

    # Try to delete a non-existent task
    result = task_manager.delete_task(999)

    # Verify the result is False
    assert result is False

    # Verify the existing task is still there
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == existing_task.id


def test_delete_task_invalid_id():
    """Test that deleting with invalid ID raises ValueError."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task("Existing Task", "Description")

    # Attempt to delete with invalid IDs
    invalid_ids = [0, -1]

    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.delete_task(invalid_id)


def test_delete_multiple_tasks():
    """Test deleting multiple tasks."""
    task_manager = TaskManager()

    # Add multiple tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3", "Description 3")

    # Verify all tasks exist
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 3

    # Delete one task
    result = task_manager.delete_task(task2.id)
    assert result is True

    # Verify only two tasks remain
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 2

    # Verify the correct task was deleted
    task_ids = [task.id for task in all_tasks]
    assert task2.id not in task_ids
    assert task1.id in task_ids
    assert task3.id in task_ids


def test_delete_all_tasks():
    """Test deleting all tasks."""
    task_manager = TaskManager()

    # Add multiple tasks
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


def test_toggle_task_status_basic():
    """Test basic functionality of toggling task status."""
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


def test_toggle_task_status_nonexistent():
    """Test that toggling status of a non-existent task raises ValueError."""
    task_manager = TaskManager()

    # Add a task
    task = task_manager.add_task("Existing Task", "Description")

    # Try to toggle a non-existent task
    with pytest.raises(ValueError, match="Task with ID 999 does not exist"):
        task_manager.toggle_task_status(999)


def test_toggle_task_status_invalid_id():
    """Test that toggling with invalid ID raises ValueError."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task("Existing Task", "Description")

    # Attempt to toggle with invalid IDs
    invalid_ids = [0, -1]

    for invalid_id in invalid_ids:
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            task_manager.toggle_task_status(invalid_id)