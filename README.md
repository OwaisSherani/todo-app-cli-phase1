# Todo CLI Application

A command-line todo application that allows users to manage tasks in memory. The application supports progressive feature levels: Basic (core operations), Intermediate (organization & usability), and Advanced (intelligent features).

## Application Levels

### Basic Level (Core Essentials)
- Add new tasks with title and optional description
- View all tasks with ID, title, and completion status
- Update existing tasks by ID
- Delete tasks by ID
- Mark tasks as complete/incomplete

### Intermediate Level (Organization & Usability)
- Priorities and Tags/Categories
  - Tasks may be assigned priority levels (High, Medium, Low)
  - Tasks may include one or more tags or categories (e.g., work, personal, home)
- Search and Filter
  - Search tasks by keyword (title or description)
  - Filter tasks by completion status, priority level, tag, or date
- Sort Tasks
  - Allow task ordering by alphabetical order, priority level, or due date

### Advanced Level (Intelligent Features)
- Recurring Tasks
  - Support tasks that repeat on a defined schedule (daily, weekly, monthly)
  - Automatically reschedule the next occurrence upon completion
- Due Dates and Time Reminders
  - Tasks may include a due date and time
  - The system tracks upcoming deadlines
  - Notifications for time-sensitive tasks

## Prerequisites

- Python 3.13 or higher

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
2. **View Task List**: Displays all tasks with ID, title, and completion status
3. **Update Task**: Modifies an existing task
4. **Delete Task**: Removes a task
5. **Mark Task Complete/Incomplete**: Toggles the completion status of a task
6. **Exit**: Exits the application

## Architecture

The application follows clean architecture principles with separation of concerns:

- **Models**: Data structures (src/models/)
- **Services**: Business logic (src/services/)
- **CLI**: User interface (src/cli/)

## License

This project is open source and available under the MIT License.