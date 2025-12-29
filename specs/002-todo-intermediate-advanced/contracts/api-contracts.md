# API Contracts: Todo In-Memory Python Console Application (Intermediate & Advanced Levels)

## Task Management Contracts

### Add Task with Extended Properties
- **Endpoint**: `add_task(title: str, description: str = None, priority: str = "Medium", tags: List[str] = [], due_date: str = None, recurrence_pattern: str = None)`
- **Input**: Task properties including priority, tags, due date, and recurrence
- **Output**: Task object with assigned ID
- **Error cases**: Invalid priority, invalid recurrence pattern, invalid date format

### Update Task with Extended Properties
- **Endpoint**: `update_task(task_id: int, **kwargs)`
- **Input**: Task ID and properties to update
- **Output**: Updated task object
- **Error cases**: Invalid task ID, invalid property values

### Search Tasks
- **Endpoint**: `search_tasks(keyword: str)`
- **Input**: Search keyword
- **Output**: List of matching task objects
- **Error cases**: None

### Filter Tasks
- **Endpoint**: `filter_tasks(filters: dict)`
- **Input**: Dictionary of filter criteria
- **Output**: List of matching task objects
- **Error cases**: Invalid filter criteria

### Sort Tasks
- **Endpoint**: `sort_tasks(sort_by: str, ascending: bool = True)`
- **Input**: Sort criteria and direction
- **Output**: List of sorted task objects
- **Error cases**: Invalid sort criteria

### Get Recurring Tasks
- **Endpoint**: `get_recurring_tasks()`
- **Input**: None
- **Output**: List of recurring task objects
- **Error cases**: None

### Get Overdue Tasks
- **Endpoint**: `get_overdue_tasks()`
- **Input**: None
- **Output**: List of overdue task objects
- **Error cases**: None

## CLI Command Contracts

### Set Task Priority
- **Command**: `set_priority <task_id> <priority>`
- **Input**: Task ID and priority level (High, Medium, Low)
- **Output**: Confirmation message
- **Error cases**: Invalid task ID, invalid priority level

### Add Task Tags
- **Command**: `add_tags <task_id> <tag1> [tag2] [tag3]...`
- **Input**: Task ID and one or more tags
- **Output**: Confirmation message
- **Error cases**: Invalid task ID

### Search Command
- **Command**: `search <keyword>`
- **Input**: Search keyword
- **Output**: List of matching tasks
- **Error cases**: None

### Filter Command
- **Command**: `filter --status=<status> --priority=<priority> --tag=<tag> --due=<date>`
- **Input**: One or more filter criteria
- **Output**: List of matching tasks
- **Error cases**: Invalid filter values

### Sort Command
- **Command**: `sort --by=<criteria> --order=<asc|desc>`
- **Input**: Sort criteria and order
- **Output**: List of sorted tasks
- **Error cases**: Invalid sort criteria or order

### Set Due Date
- **Command**: `set_due_date <task_id> <date>`
- **Input**: Task ID and date in YYYY-MM-DD format
- **Output**: Confirmation message
- **Error cases**: Invalid task ID, invalid date format

### Set Recurrence
- **Command**: `set_recurrence <task_id> <pattern>`
- **Input**: Task ID and recurrence pattern (daily, weekly, monthly)
- **Output**: Confirmation message
- **Error cases**: Invalid task ID, invalid recurrence pattern

### Show Reminders
- **Command**: `reminders`
- **Input**: None
- **Output**: List of upcoming and overdue tasks
- **Error cases**: None