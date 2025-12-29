# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites
- Python 3.13 or higher installed on your system

## Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.13+ available in your environment

## Running the Application
```bash
cd src/cli
python main.py
```

## Using the Application
The application provides a menu-driven interface:

1. **Add Task**: Creates a new task with a title and optional description
   - Prompts for task title (required)
   - Prompts for task description (optional)

2. **View Task List**: Displays all tasks with ID, title, and completion status

3. **Update Task**: Modifies an existing task
   - Prompts for task ID
   - Prompts for new title (optional, press Enter to keep current)
   - Prompts for new description (optional, press Enter to keep current)

4. **Delete Task**: Removes a task
   - Prompts for task ID to delete

5. **Mark Task Complete/Incomplete**: Toggles the completion status of a task
   - Prompts for task ID
   - Toggles the completion status

6. **Exit**: Exits the application

## Example Usage
```
Welcome to the Todo CLI Application!
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Need to buy milk, bread, and eggs
Task added successfully with ID: 1
```

## Error Handling
- Invalid inputs are handled gracefully with user-friendly error messages
- Non-existent task IDs will result in appropriate error messages
- Empty titles will be rejected when adding or updating tasks