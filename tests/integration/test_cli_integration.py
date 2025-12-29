"""
Integration test for add task feature in the CLI.
"""
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.cli.main import TodoCLI
from src.services.task_manager import TaskManager


def test_add_task_integration():
    """Test the full integration of adding a task through the CLI."""
    # Create a CLI instance
    cli = TodoCLI()
    
    # Initially, there should be no tasks
    assert len(cli.task_manager.get_all_tasks()) == 0
    
    # Add a task
    title = "Integration Test Task"
    description = "This is an integration test description"
    
    task = cli.task_manager.add_task(title, description)
    
    # Verify the task was added
    assert task.title == title
    assert task.description == description
    assert task.completed is False
    assert task.id == 1
    
    # Verify the task is in the manager's list
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == 1
    assert all_tasks[0].title == title
    assert all_tasks[0].description == description


def test_cli_add_task_simulation():
    """Simulate adding a task through CLI input."""
    # Create a CLI instance
    cli = TodoCLI()
    
    # Mock user inputs for adding a task
    inputs = ["Integration Test Task", "This is a simulated description"]
    
    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        cli.handle_add_task()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify the task was added
        all_tasks = cli.task_manager.get_all_tasks()
        assert len(all_tasks) == 1
        task = all_tasks[0]
        assert task.title == "Integration Test Task"
        assert task.description == "This is a simulated description"
        assert task.completed is False
        assert task.id == 1


def test_cli_add_task_empty_title():
    """Test CLI behavior when adding a task with empty title."""
    # Create a CLI instance
    cli = TodoCLI()

    # Mock user inputs for adding a task with empty title
    inputs = ["", "This description won't matter"]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_add_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify no task was added due to validation
        all_tasks = cli.task_manager.get_all_tasks()
        assert len(all_tasks) == 0


def test_view_task_list_integration():
    """Test the full integration of viewing task list through the CLI."""
    # Create a CLI instance
    cli = TodoCLI()

    # Initially, there should be no tasks
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 0

    # Add a few tasks
    task1 = cli.task_manager.add_task("Task 1", "Description 1")
    task2 = cli.task_manager.add_task("Task 2", "Description 2")
    task3 = cli.task_manager.add_task("Task 3")

    # Verify the tasks are in the manager
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 3

    # Check that the tasks have the expected properties
    assert all_tasks[0].id == task1.id
    assert all_tasks[0].title == "Task 1"
    assert all_tasks[0].description == "Description 1"

    assert all_tasks[1].id == task2.id
    assert all_tasks[1].title == "Task 2"
    assert all_tasks[1].description == "Description 2"

    assert all_tasks[2].id == task3.id
    assert all_tasks[2].title == "Task 3"
    assert all_tasks[2].description == ""


def test_cli_view_task_list_simulation():
    """Simulate viewing task list through CLI."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add some tasks
    cli.task_manager.add_task("Task 1", "Description 1")
    cli.task_manager.add_task("Task 2")

    # Capture printed output when viewing tasks
    captured_output = StringIO()
    sys.stdout = captured_output

    cli.handle_view_tasks()

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    # Verify the output contains the expected information
    assert "Task 1" in output
    assert "Description 1" in output
    assert "Task 2" in output
    assert "No tasks found" not in output  # Since we have tasks


def test_cli_view_empty_task_list():
    """Test CLI behavior when viewing an empty task list."""
    # Create a CLI instance
    cli = TodoCLI()

    # Ensure no tasks exist
    assert len(cli.task_manager.get_all_tasks()) == 0

    # Capture printed output when viewing tasks
    captured_output = StringIO()
    sys.stdout = captured_output

    cli.handle_view_tasks()

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    # Verify the output indicates no tasks
    assert "No tasks found" in output


def test_update_task_integration():
    """Test the full integration of updating a task through the CLI."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task to update
    original_task = cli.task_manager.add_task("Original Title", "Original Description")

    # Verify the task was added
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].title == "Original Title"
    assert all_tasks[0].description == "Original Description"

    # Update the task using the CLI manager directly
    new_title = "Updated Title"
    new_description = "Updated Description"
    updated_task = cli.task_manager.update_task(original_task.id, new_title, new_description)

    # Verify the task was updated
    assert updated_task.title == new_title
    assert updated_task.description == new_description
    assert updated_task.id == original_task.id  # ID should remain the same


def test_cli_update_task_simulation():
    """Simulate updating a task through CLI input."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task to update
    task = cli.task_manager.add_task("Original Title", "Original Description")

    # Mock user inputs for updating a task
    inputs = [str(task.id), "Updated Title", "Updated Description"]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_update_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the task was updated
        updated_task = cli.task_manager.get_task_by_id(task.id)
        assert updated_task is not None
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Updated Description"


def test_cli_update_nonexistent_task():
    """Test CLI behavior when trying to update a non-existent task."""
    # Create a CLI instance
    cli = TodoCLI()

    # Mock user inputs for updating a non-existent task
    inputs = ["999", "Updated Title", "Updated Description"]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_update_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Verify the error message is shown
        assert "not found" in output.lower()


def test_cli_update_task_keep_fields():
    """Test CLI behavior when updating a task but keeping some fields."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task to update
    task = cli.task_manager.add_task("Original Title", "Original Description")

    # Mock user inputs for updating only the title (keeping description)
    inputs = [str(task.id), "Updated Title", ""]  # Empty string to keep current description

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_update_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the task was updated with new title but kept description
        updated_task = cli.task_manager.get_task_by_id(task.id)
        assert updated_task is not None
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Original Description"  # Should remain unchanged


def test_delete_task_integration():
    """Test the full integration of deleting a task through the CLI."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task to delete
    task = cli.task_manager.add_task("Task to Delete", "Description to Delete")

    # Verify the task was added
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == task.id

    # Delete the task using the CLI manager directly
    result = cli.task_manager.delete_task(task.id)

    # Verify the task was deleted
    assert result is True

    # Verify the task is no longer in the list
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 0


def test_cli_delete_task_simulation():
    """Simulate deleting a task through CLI input."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task to delete
    task = cli.task_manager.add_task("Task to Delete", "Description")

    # Verify the task exists
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 1

    # Mock user inputs for deleting a task
    inputs = [str(task.id)]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_delete_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the task was deleted
        all_tasks = cli.task_manager.get_all_tasks()
        assert len(all_tasks) == 0


def test_cli_delete_nonexistent_task():
    """Test CLI behavior when trying to delete a non-existent task."""
    # Create a CLI instance
    cli = TodoCLI()

    # Mock user inputs for deleting a non-existent task
    inputs = ["999"]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_delete_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Verify the error message is shown
        assert "not found" in output.lower()


def test_cli_delete_multiple_tasks():
    """Test CLI behavior when deleting multiple tasks."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add multiple tasks
    task1 = cli.task_manager.add_task("Task 1", "Description 1")
    task2 = cli.task_manager.add_task("Task 2", "Description 2")
    task3 = cli.task_manager.add_task("Task 3", "Description 3")

    # Verify all tasks exist
    all_tasks = cli.task_manager.get_all_tasks()
    assert len(all_tasks) == 3

    # Delete one task
    inputs = [str(task2.id)]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_delete_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify only one task was deleted
        all_tasks = cli.task_manager.get_all_tasks()
        assert len(all_tasks) == 2

        # Verify the correct task was deleted
        task_ids = [task.id for task in all_tasks]
        assert task2.id not in task_ids
        assert task1.id in task_ids
        assert task3.id in task_ids


def test_toggle_task_status_integration():
    """Test the full integration of toggling task status through the CLI."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task
    task = cli.task_manager.add_task("Test Task", "Test Description")

    # Verify initial state
    assert task.completed is False

    # Toggle the status using the CLI manager directly
    cli.task_manager.toggle_task_status(task.id)

    # Verify the status was toggled
    updated_task = cli.task_manager.get_task_by_id(task.id)
    assert updated_task.completed is True

    # Toggle back to pending
    cli.task_manager.toggle_task_status(task.id)

    # Verify the status was toggled back
    updated_task = cli.task_manager.get_task_by_id(task.id)
    assert updated_task.completed is False


def test_cli_toggle_task_status_simulation():
    """Simulate toggling task status through CLI input."""
    # Create a CLI instance
    cli = TodoCLI()

    # Add a task
    task = cli.task_manager.add_task("Test Task", "Test Description")

    # Verify initial state
    assert task.completed is False

    # Mock user inputs for toggling task status
    inputs = [str(task.id)]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_toggle_task_status()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the status was toggled
        updated_task = cli.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is True

        # Toggle back to pending
        with patch('builtins.input', side_effect=[str(task.id)]):
            cli.handle_toggle_task_status()

        # Verify the status was toggled back
        updated_task = cli.task_manager.get_task_by_id(task.id)
        assert updated_task.completed is False


def test_cli_toggle_nonexistent_task():
    """Test CLI behavior when trying to toggle status of a non-existent task."""
    # Create a CLI instance
    cli = TodoCLI()

    # Mock user inputs for toggling status of a non-existent task
    inputs = ["999"]

    with patch('builtins.input', side_effect=inputs):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        cli.handle_toggle_task_status()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Verify the error message is shown
        assert "not found" in output.lower()