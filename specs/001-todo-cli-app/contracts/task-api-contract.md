# API Contracts: Todo In-Memory Python Console Application

## Task Operations

### Add Task
- **Input**: title (string, required), description (string, optional)
- **Output**: task object with id, title, description, completed status
- **Errors**: Invalid input (empty title)

### View Task List
- **Input**: None
- **Output**: List of task objects
- **Errors**: None

### Update Task
- **Input**: task_id (integer), title (string, optional), description (string, optional)
- **Output**: Updated task object
- **Errors**: Task not found, invalid task ID

### Delete Task
- **Input**: task_id (integer)
- **Output**: Success confirmation
- **Errors**: Task not found, invalid task ID

### Toggle Task Status
- **Input**: task_id (integer)
- **Output**: Updated task object
- **Errors**: Task not found, invalid task ID

## Task Object Schema
```
{
  "id": integer,
  "title": string,
  "description": string,
  "completed": boolean
}
```

## Error Response Schema
```
{
  "error": string,
  "code": string
}
```