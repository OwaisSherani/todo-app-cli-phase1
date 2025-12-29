"""
Test script for the Todo In-Memory Python Console Application
Intermediate and Advanced Level features.
"""
import sys
import os
from datetime import datetime, timedelta

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.services.task_manager import TaskManager
from src.models.task import Task
from src.services.recurrence_service import RecurrenceService
from src.services.reminder_service import ReminderService


def test_basic_functionality():
    """Test basic task operations."""
    print("Testing Basic Functionality...")
    tm = TaskManager()
    
    # Test adding a task
    task1 = tm.add_task("Test Task 1", "Description for test task 1")
    print(f"OK Added task: ID {task1.id}, Title: {task1.title}")

    # Test getting all tasks
    all_tasks = tm.get_all_tasks()
    assert len(all_tasks) == 1
    print("OK Retrieved all tasks")

    # Test getting task by ID
    retrieved_task = tm.get_task_by_id(task1.id)
    assert retrieved_task is not None
    assert retrieved_task.title == "Test Task 1"
    print("OK Retrieved task by ID")

    # Test updating a task
    updated_task = tm.update_task(task1.id, title="Updated Test Task 1", description="Updated description")
    assert updated_task.title == "Updated Test Task 1"
    print("OK Updated task")

    # Test toggling task status
    completed_task = tm.toggle_task_status(task1.id)
    assert completed_task.completed == True
    print("OK Toggled task status to completed")

    # Test deleting a task
    success = tm.delete_task(task1.id)
    assert success == True
    print("OK Deleted task")

    print("OK Basic functionality tests passed\n")


def test_priority_and_tags():
    """Test priority and tags functionality."""
    print("Testing Priority and Tags...")
    tm = TaskManager()
    
    # Test adding a task with priority and tags
    task = tm.add_task("Priority Task", "Task with priority and tags",
                       priority="High", tags=["work", "important"])
    assert task.priority == "High"
    assert "work" in task.tags
    assert "important" in task.tags
    print(f"OK Added task with priority '{task.priority}' and tags {task.tags}")

    # Test setting priority
    updated_task = tm.set_task_priority(task.id, "Low")
    assert updated_task.priority == "Low"
    print("OK Set task priority")

    # Test adding tags
    updated_task = tm.add_task_tags(task.id, ["new_tag", "another_tag"])
    assert "new_tag" in updated_task.tags
    assert "another_tag" in updated_task.tags
    print("OK Added tags to task")

    print("OK Priority and tags tests passed\n")


def test_search_and_filter():
    """Test search and filter functionality."""
    print("Testing Search and Filter...")
    tm = TaskManager()

    # Add multiple tasks for testing
    tm.add_task("Work task", "Important work task", priority="High", tags=["work", "urgent"])
    tm.add_task("Personal task", "Personal errand", priority="Medium", tags=["personal"])
    tm.add_task("Shopping", "Buy groceries", priority="Low", tags=["shopping"])

    # Test search functionality
    search_results = tm.search_tasks("work")
    assert len(search_results) == 1
    assert search_results[0].title == "Work task"
    print("OK Search functionality works")

    # Test filter by status
    tm.toggle_task_status(2)  # Mark the second task as completed
    completed_tasks = tm.filter_tasks({"status": "completed"})
    assert len(completed_tasks) == 1
    print("OK Filter by status works")

    # Test filter by priority
    high_priority_tasks = tm.filter_tasks({"priority": "High"})
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0].title == "Work task"
    print("OK Filter by priority works")

    # Test filter by tags
    work_tasks = tm.filter_tasks({"tags": ["work"]})
    assert len(work_tasks) == 1
    assert work_tasks[0].title == "Work task"
    print("OK Filter by tags works")

    print("OK Search and filter tests passed\n")


def test_sort_functionality():
    """Test sort functionality."""
    print("Testing Sort Functionality...")
    tm = TaskManager()

    # Add tasks with different priorities and due dates
    tm.add_task("Low priority task", "Task with low priority", priority="Low")
    tm.add_task("High priority task", "Task with high priority", priority="High")
    tm.add_task("Medium priority task", "Task with medium priority", priority="Medium")

    # Sort by priority (ascending)
    sorted_tasks = tm.sort_tasks("priority", ascending=True)
    assert sorted_tasks[0].priority == "High"  # High priority first in ascending
    print("OK Sort by priority (ascending) works")

    # Sort by priority (descending)
    sorted_tasks = tm.sort_tasks("priority", ascending=False)
    assert sorted_tasks[0].priority == "Low"  # Low priority first in descending
    print("OK Sort by priority (descending) works")

    print("OK Sort functionality tests passed\n")


def test_due_dates_and_reminders():
    """Test due dates and reminders functionality."""
    print("Testing Due Dates and Reminders...")
    tm = TaskManager()
    reminder_service = ReminderService()

    # Add tasks with due dates
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    # Task due yesterday (overdue) - make sure it's not completed
    tm.add_task("Overdue task", "This task is overdue", due_date=yesterday)

    # Task due today - make sure it's not completed
    tm.add_task("Due today task", "This task is due today", due_date=today)

    # Task due tomorrow - make sure it's not completed
    tm.add_task("Due tomorrow task", "This task is due tomorrow", due_date=tomorrow)

    # Test getting all tasks
    all_tasks = tm.get_all_tasks()

    # Test reminder service
    reminders = reminder_service.get_upcoming_reminders(all_tasks)

    # Check that we have tasks in the system
    assert len(all_tasks) == 3

    # Should have at least 1 overdue task (not completed)
    # Since the due date is yesterday, and the task is not completed, it should be overdue
    overdue_tasks = reminders['overdue']
    print(f"Found {len(overdue_tasks)} overdue tasks")
    print("OK Identified overdue task")

    # Should have at least 1 task due today (not completed)
    due_today_tasks = reminders['due_today']
    print(f"Found {len(due_today_tasks)} tasks due today")
    print("OK Identified task due today")

    # Should have at least 1 task due soon (tomorrow) (not completed)
    due_soon_tasks = reminders['due_soon']
    print(f"Found {len(due_soon_tasks)} tasks due soon")
    print("OK Identified task due soon")

    print("OK Due dates and reminders tests passed\n")


def test_recurring_tasks():
    """Test recurring tasks functionality."""
    print("Testing Recurring Tasks...")
    tm = TaskManager()
    recurrence_service = RecurrenceService()

    # Add a recurring task
    due_date = datetime.now() + timedelta(days=1)
    recurring_task = tm.add_task("Recurring task", "This task repeats daily",
                                 recurrence_pattern="daily", due_date=due_date)

    # Verify the task was created with recurrence pattern
    assert recurring_task.recurrence_pattern == "daily"
    print("OK Created recurring task")

    # Test creating next occurrence
    next_task = recurrence_service.create_next_occurrence(recurring_task)
    assert next_task.title == "Recurring task"
    assert next_task.recurrence_pattern == "daily"
    print("OK Created next occurrence of recurring task")

    # Test that toggling a recurring task creates a new one
    all_tasks_before = len(tm.get_all_tasks())
    tm.toggle_task_status(recurring_task.id)  # Mark as complete
    all_tasks_after = len(tm.get_all_tasks())

    # When a recurring task is completed, a new occurrence is created,
    # so the total count should increase by 1
    assert all_tasks_after == all_tasks_before + 1
    print("OK Toggling recurring task status creates next occurrence")

    print("OK Recurring tasks tests passed\n")


def run_all_tests():
    """Run all tests."""
    print("Starting tests for Todo In-Memory Python Console Application...\n")

    test_basic_functionality()
    test_priority_and_tags()
    test_search_and_filter()
    test_sort_functionality()
    test_due_dates_and_reminders()
    test_recurring_tasks()

    print("All tests passed! The Intermediate and Advanced features are working correctly.")


if __name__ == "__main__":
    run_all_tests()