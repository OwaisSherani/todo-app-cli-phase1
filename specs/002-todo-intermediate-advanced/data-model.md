# Data Model: Todo In-Memory Python Console Application (Intermediate & Advanced Levels)

## Extended Task Model

### Task Entity
- **id**: Integer (unique, auto-incremented)
- **title**: String (required)
- **description**: String (optional)
- **status**: String (either "Pending" or "Completed", default "Pending")
- **priority**: String (optional, one of "High", "Medium", "Low", default "Medium")
- **tags**: List of Strings (optional, default empty list)
- **due_date**: DateTime (optional, default None)
- **recurrence_pattern**: String (optional, one of "daily", "weekly", "monthly", default None)
- **created_at**: DateTime (auto-generated when task is created)
- **completed_at**: DateTime (optional, set when task is marked complete)

### TaskList Entity
- **tasks**: List of Task entities
- **add_task(title: str, description: str = None, priority: str = "Medium", tags: List[str] = [], due_date: DateTime = None, recurrence_pattern: str = None)**: Adds a new task to the list
- **get_all_tasks()**: Returns all tasks
- **get_task_by_id(task_id: int)**: Returns a specific task by ID
- **update_task(task_id: int, **kwargs)**: Updates a task's properties
- **delete_task(task_id: int)**: Removes a task from the list
- **mark_task_complete(task_id: int)**: Marks a task as complete
- **mark_task_incomplete(task_id: int)**: Marks a task as incomplete
- **search_tasks(keyword: str)**: Returns tasks matching the keyword in title or description
- **filter_tasks(filters: dict)**: Returns tasks matching the specified filters (status, priority, tags, due_date)
- **sort_tasks(sort_by: str, ascending: bool = True)**: Returns tasks sorted by the specified criteria
- **get_recurring_tasks()**: Returns all tasks with recurrence patterns
- **get_overdue_tasks()**: Returns tasks that are past their due date and still pending

## State Transitions

### Task Status Transitions
- Pending → Completed (when user marks task as complete)
- Completed → Pending (when user marks task as incomplete)

### Task Creation/Deletion
- New task → Added to task list (with Pending status)
- Task deletion → Removed from task list

### Recurring Task Transitions
- Completed recurring task → New instance created based on recurrence pattern
- New recurring task instance → Added to task list (with Pending status)

## Validation Rules

### Task Creation
- Title is required and must not be empty
- Priority must be one of "High", "Medium", "Low" if provided
- Tags must be a list of strings if provided
- Due date must be a valid datetime if provided
- Recurrence pattern must be one of "daily", "weekly", "monthly" if provided

### Task Updates
- ID cannot be changed
- Status can only be "Pending" or "Completed"
- Priority must be one of "High", "Medium", "Low" if provided
- Tags must be a list of strings if provided
- Due date must be a valid datetime if provided
- Recurrence pattern must be one of "daily", "weekly", "monthly" if provided

### Task Operations
- Operations (update, delete, mark complete) require a valid task ID that exists in the list
- Completed tasks can be marked as incomplete
- Incomplete tasks can be marked as complete
- Recurring tasks can be modified to change their recurrence pattern