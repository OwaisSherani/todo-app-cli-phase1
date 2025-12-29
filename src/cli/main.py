"""
Command-line interface for the Todo CLI Application with extended features.
"""
import sys
import os
from datetime import datetime
from typing import Optional, List

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_manager import TaskManager
from src.models.task import Task
from src.lib.utils import format_task_display
from src.services.reminder_service import ReminderService


class TodoCLI:
    """
    Command-line interface for the Todo application with extended features.
    """

    def __init__(self):
        """Initialize the CLI with a TaskManager."""
        self.task_manager = TaskManager()
        self.reminder_service = ReminderService()

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("Welcome to the Todo CLI Application!")
        print("Extended with Intermediate & Advanced Features")
        print("="*50)
        print("1.  Add Task")
        print("2.  View Task List")
        print("3.  Update Task")
        print("4.  Delete Task")
        print("5.  Mark Task Complete/Incomplete")
        print("6.  Set Task Priority")
        print("7.  Add Task Tags")
        print("8.  Search Tasks")
        print("9.  Filter Tasks")
        print("10. Sort Tasks")
        print("11. Set Recurrence")
        print("12. Set Due Date")
        print("13. View Reminders")
        print("14. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            str: User's menu choice
        """
        try:
            choice = input("Choose an option (1-14): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            sys.exit(0)

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.handle_add_task()
            elif choice == '2':
                self.handle_view_tasks()
            elif choice == '3':
                self.handle_update_task()
            elif choice == '4':
                self.handle_delete_task()
            elif choice == '5':
                self.handle_toggle_task_status()
            elif choice == '6':
                self.handle_set_priority()
            elif choice == '7':
                self.handle_add_tags()
            elif choice == '8':
                self.handle_search_tasks()
            elif choice == '9':
                self.handle_filter_tasks()
            elif choice == '10':
                self.handle_sort_tasks()
            elif choice == '11':
                self.handle_set_recurrence()
            elif choice == '12':
                self.handle_set_due_date()
            elif choice == '13':
                self.handle_view_reminders()
            elif choice == '14':
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 14.")

    def handle_add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()

            # Get priority
            priority = input("Enter priority (High/Medium/Low, default: Medium): ").strip()
            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"

            task = self.task_manager.add_task(title, description, priority)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- Task List ---")
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            print(format_task_display(task))
            print()

    def handle_update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)

            # Get current task to show current values
            current_task = self.task_manager.get_task_by_id(task_id)
            if not current_task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            print(f"Current title: {current_task.title}")
            new_title = input("Enter new title (press Enter to keep current): ").strip()
            if new_title == "":
                new_title = current_task.title

            print(f"Current description: {current_task.description}")
            new_description = input("Enter new description (press Enter to keep current): ").strip()
            if new_description == "":
                new_description = current_task.description

            updated_task = self.task_manager.update_task(task_id, title=new_title, description=new_description)
            print(f"Task {task_id} updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            self.task_manager.delete_task(task_id)
            print(f"Task {task_id} deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_toggle_task_status(self):
        """Handle toggling task completion status."""
        print("\n--- Toggle Task Status ---")
        try:
            task_id_input = input("Enter task ID to toggle status: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            self.task_manager.toggle_task_status(task_id)
            new_status = "completed" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {new_status}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_set_priority(self):
        """Handle setting task priority."""
        print("\n--- Set Task Priority ---")
        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            priority = input("Enter priority (High/Medium/Low): ").strip()
            if priority not in ["High", "Medium", "Low"]:
                print("Error: Priority must be one of: High, Medium, Low")
                return

            self.task_manager.set_task_priority(task_id, priority)
            print(f"Priority for task {task_id} set to {priority}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_add_tags(self):
        """Handle adding tags to a task."""
        print("\n--- Add Task Tags ---")
        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            tags_input = input("Enter tags (comma-separated): ").strip()
            if not tags_input:
                print("Error: Tags cannot be empty.")
                return

            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            if not tags:
                print("Error: No valid tags provided.")
                return

            self.task_manager.add_task_tags(task_id, tags)
            print(f"Tags added to task {task_id}: {', '.join(tags)}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_search_tasks(self):
        """Handle searching tasks."""
        print("\n--- Search Tasks ---")
        try:
            keyword = input("Enter search keyword: ").strip()
            if not keyword:
                print("Error: Search keyword cannot be empty.")
                return

            tasks = self.task_manager.search_tasks(keyword)
            if not tasks:
                print("No matching tasks found.")
                return

            print(f"Found {len(tasks)} matching task(s):")
            for task in tasks:
                print(format_task_display(task))
                print()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_filter_tasks(self):
        """Handle filtering tasks."""
        print("\n--- Filter Tasks ---")
        try:
            print("Filter options:")
            status = input("Status (completed/pending, press Enter to skip): ").strip()
            priority = input("Priority (High/Medium/Low, press Enter to skip): ").strip()
            tag = input("Tag (press Enter to skip): ").strip()
            due_date_str = input("Due date (YYYY-MM-DD, press Enter to skip): ").strip()

            filters = {}
            if status in ["completed", "pending"]:
                filters["status"] = status
            if priority in ["High", "Medium", "Low"]:
                filters["priority"] = priority
            if tag:
                filters["tags"] = [tag]
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                    filters["due_date"] = due_date
                except ValueError:
                    print("Error: Invalid date format. Use YYYY-MM-DD.")
                    return

            tasks = self.task_manager.filter_tasks(filters)
            if not tasks:
                print("No matching tasks found.")
                return

            print(f"Found {len(tasks)} matching task(s):")
            for task in tasks:
                print(format_task_display(task))
                print()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_sort_tasks(self):
        """Handle sorting tasks."""
        print("\n--- Sort Tasks ---")
        try:
            print("Sort by options:")
            print("1. Due date")
            print("2. Priority")
            print("3. Title")
            sort_choice = input("Choose sort option (1-3): ").strip()

            if sort_choice == '1':
                sort_by = 'due_date'
            elif sort_choice == '2':
                sort_by = 'priority'
            elif sort_choice == '3':
                sort_by = 'title'
            else:
                print("Error: Invalid sort option. Choose 1, 2, or 3.")
                return

            order_choice = input("Order (asc/desc, default: asc): ").strip().lower()
            ascending = order_choice != 'desc'

            tasks = self.task_manager.sort_tasks(sort_by, ascending)
            if not tasks:
                print("No tasks to sort.")
                return

            print(f"Tasks sorted by {sort_by} ({'ascending' if ascending else 'descending'}):")
            for task in tasks:
                print(format_task_display(task))
                print()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_set_recurrence(self):
        """Handle setting recurrence for a task."""
        print("\n--- Set Recurrence ---")
        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            print("Recurrence options:")
            print("1. daily")
            print("2. weekly")
            print("3. monthly")
            recurrence_choice = input("Choose recurrence option (1-3): ").strip()

            if recurrence_choice == '1':
                recurrence_pattern = 'daily'
            elif recurrence_choice == '2':
                recurrence_pattern = 'weekly'
            elif recurrence_choice == '3':
                recurrence_pattern = 'monthly'
            else:
                print("Error: Invalid recurrence option. Choose 1, 2, or 3.")
                return

            self.task_manager.set_task_recurrence(task_id, recurrence_pattern)
            print(f"Recurrence for task {task_id} set to {recurrence_pattern}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_set_due_date(self):
        """Handle setting due date for a task."""
        print("\n--- Set Due Date ---")
        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            due_date_str = input("Enter due date (YYYY-MM-DD): ").strip()
            if not due_date_str:
                print("Error: Due date cannot be empty.")
                return

            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid date format. Use YYYY-MM-DD.")
                return

            self.task_manager.set_task_due_date(task_id, due_date)
            print(f"Due date for task {task_id} set to {due_date_str}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_view_reminders(self):
        """Handle viewing reminders for upcoming and overdue tasks."""
        print("\n--- Reminders ---")
        try:
            # Get all tasks
            all_tasks = self.task_manager.get_all_tasks()

            # Get reminders using the reminder service
            reminders = self.reminder_service.get_upcoming_reminders(all_tasks)

            # Display overdue tasks
            overdue_tasks = reminders['overdue']
            if overdue_tasks:
                print(f"Overdue Tasks ({len(overdue_tasks)}):")
                for task in overdue_tasks:
                    print(format_task_display(task))
                    print()
            else:
                print("No overdue tasks.")

            # Display tasks due today
            due_today_tasks = reminders['due_today']
            if due_today_tasks:
                print(f"Tasks Due Today ({len(due_today_tasks)}):")
                for task in due_today_tasks:
                    print(format_task_display(task))
                    print()
            else:
                print("No tasks due today.")

            # Display tasks due soon
            due_soon_tasks = reminders['due_soon']
            if due_soon_tasks:
                print(f"Tasks Due Soon ({len(due_soon_tasks)}):")
                for task in due_soon_tasks:
                    print(format_task_display(task))
                    print()
            else:
                print("No tasks due soon.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()