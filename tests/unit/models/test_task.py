"""
Unit tests for the Task model.
"""
import pytest
from src.models.task import Task


def test_task_creation():
    """Test creating a Task with valid parameters."""
    task = Task(id=1, title="Test Task")
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is False


def test_task_creation_with_description():
    """Test creating a Task with description."""
    task = Task(id=1, title="Test Task", description="Test Description")
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


def test_task_creation_with_completed_status():
    """Test creating a Task with completed status."""
    task = Task(id=1, title="Test Task", completed=True)
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is True


def test_task_validation_id():
    """Test Task validation for ID."""
    # Valid ID
    Task(id=1, title="Test Task")
    
    # Invalid ID - non-integer
    with pytest.raises(ValueError, match="Task ID must be a positive integer"):
        Task(id="invalid", title="Test Task")
    
    # Invalid ID - zero
    with pytest.raises(ValueError, match="Task ID must be a positive integer"):
        Task(id=0, title="Test Task")
    
    # Invalid ID - negative
    with pytest.raises(ValueError, match="Task ID must be a positive integer"):
        Task(id=-1, title="Test Task")


def test_task_validation_title():
    """Test Task validation for title."""
    # Valid title
    Task(id=1, title="Test Task")
    
    # Invalid title - empty string
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        Task(id=1, title="")
    
    # Invalid title - only whitespace
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        Task(id=1, title="   ")
    
    # Invalid title - non-string
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        Task(id=1, title=123)


def test_task_validation_description():
    """Test Task validation for description."""
    # Valid description - string
    Task(id=1, title="Test Task", description="Valid description")
    
    # Valid description - empty string
    Task(id=1, title="Test Task", description="")
    
    # Invalid description - non-string
    with pytest.raises(ValueError, match="Task description must be a string"):
        Task(id=1, title="Test Task", description=123)


def test_task_validation_completed():
    """Test Task validation for completed status."""
    # Valid completed - boolean
    Task(id=1, title="Test Task", completed=True)
    Task(id=1, title="Test Task", completed=False)
    
    # Invalid completed - non-boolean
    with pytest.raises(ValueError, match="Task completion status must be a boolean"):
        Task(id=1, title="Test Task", completed="true")


def test_mark_complete():
    """Test marking a task as complete."""
    task = Task(id=1, title="Test Task")
    assert task.completed is False
    
    task.mark_complete()
    assert task.completed is True


def test_mark_incomplete():
    """Test marking a task as incomplete."""
    task = Task(id=1, title="Test Task", completed=True)
    assert task.completed is True
    
    task.mark_incomplete()
    assert task.completed is False


def test_update_task():
    """Test updating task title and description."""
    task = Task(id=1, title="Original Title", description="Original Description")
    
    # Update title only
    task.update(title="New Title")
    assert task.title == "New Title"
    assert task.description == "Original Description"
    
    # Update description only
    task.update(description="New Description")
    assert task.title == "New Title"
    assert task.description == "New Description"
    
    # Update both
    task.update(title="Final Title", description="Final Description")
    assert task.title == "Final Title"
    assert task.description == "Final Description"


def test_update_task_validation():
    """Test validation during task update."""
    task = Task(id=1, title="Original Title")
    
    # Valid updates
    task.update(title="New Title")
    assert task.title == "New Title"
    
    task.update(description="New Description")
    assert task.description == "New Description"
    
    # Invalid title update
    with pytest.raises(ValueError, match="Task title must be a non-empty string"):
        task.update(title="")
    
    # Invalid description update
    with pytest.raises(ValueError, match="Task description must be a string"):
        task.update(description=123)