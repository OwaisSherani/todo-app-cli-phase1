"""
Contract test for view task list functionality.
"""
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_view_task_list_contract():
    """Test that view task list functionality meets the contract specifications."""
    task_manager = TaskManager()
    
    # Initially, the task list should be empty
    tasks = task_manager.get_all_tasks()
    assert tasks == []
    assert len(tasks) == 0
    
    # Add a few tasks
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")
    task3 = task_manager.add_task("Task 3")
    
    # Get all tasks
    tasks = task_manager.get_all_tasks()
    
    # Verify the list contains all tasks
    assert len(tasks) == 3
    assert tasks[0].id == task1.id
    assert tasks[1].id == task2.id
    assert tasks[2].id == task3.id
    
    # Verify task properties are preserved
    assert tasks[0].title == "Task 1"
    assert tasks[0].description == "Description 1"
    assert tasks[0].completed is False
    
    assert tasks[1].title == "Task 2"
    assert tasks[1].description == "Description 2"
    assert tasks[1].completed is False
    
    assert tasks[2].title == "Task 3"
    assert tasks[2].description == ""
    assert tasks[2].completed is False
    
    # Verify that the returned list is a copy (not the internal list)
    original_internal_list = task_manager.tasks
    returned_list = task_manager.get_all_tasks()
    assert returned_list is not original_internal_list
    
    # Modifying the returned list should not affect the internal list
    returned_list_copy = returned_list.copy()
    if returned_list:
        returned_list.pop()
        # Internal list should still have all tasks
        assert len(task_manager.get_all_tasks()) == 3