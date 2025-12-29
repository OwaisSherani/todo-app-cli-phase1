# Data Model: Todo In-Memory Python Console Application

## Task Entity

### Fields
- **id** (integer): Unique identifier for the task, automatically assigned
- **title** (string): Required title of the task
- **description** (string): Optional description of the task (default: "")
- **completed** (boolean): Completion status of the task (default: False)

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string
- Description can be any string (including empty)
- Completed status must be a boolean value

### State Transitions
- A task starts with `completed = False`
- A task can transition from `completed = False` to `completed = True` (mark as complete)
- A task can transition from `completed = True` to `completed = False` (mark as incomplete)

## TaskList Entity

### Fields
- **tasks** (list): Collection of Task objects
- **next_id** (integer): Counter for generating unique IDs (starts at 1)

### Operations
- **add_task(title, description)**: Creates a new task with the next available ID
- **get_all_tasks()**: Returns all tasks in the collection
- **get_task_by_id(task_id)**: Returns a specific task by its ID
- **update_task(task_id, title, description)**: Updates an existing task's information
- **delete_task(task_id)**: Removes a task from the collection
- **toggle_task_status(task_id)**: Toggles the completion status of a task

### Validation Rules
- Task ID must exist in the collection before update, delete, or toggle operations
- Title must not be empty when creating or updating a task