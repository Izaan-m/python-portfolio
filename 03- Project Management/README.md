# Business Project Management System

A terminal-based project management application built with Python to manage projects, assign tasks, track deadlines and monitor project progress.

This is the third project in my Python portfolio. The objective was to apply Python fundamentals to a practical business problem inspired by project coordination and consulting workflows.

## Features

- Create projects with automatically generated project IDs, client details, project managers and deadlines.
- View all registered projects and their current statuses.
- Add tasks with unique IDs within each project, descriptions, deadlines and priorities.
- Assign tasks to team members.
- View all tasks associated with a project.
- Update task statuses: Pending, In Progress or Completed.
- Automatically update the overall project status based on task statuses.
- Calculate project completion percentages.
- Search projects by ID, project name or client name.
- Identify unfinished tasks past their deadlines.
- Generate project reports with task counts, completion percentages and overdue task counts.
- Validate IDs, required text fields, dates, priorities and task statuses.

## Technologies Used

- Python 3.10 or later
- Python standard library: `datetime` and `unittest`
- Visual Studio Code

No external packages are required. The application was tested with Python 3.13.5.

## Python Concepts Used

- Variables and data types
- Conditional statements and logical operators
- For and while loops
- Match-case statements
- Functions, parameters and return values
- Lists, dictionaries and nested data structures
- Dictionary methods and membership checks
- F-strings and string methods
- Running counters and percentage calculations
- Date parsing and comparison
- Exception handling and input validation
- Modular programming and automated testing

## Application Menu

```text
====== Welcome to Project Management System ======
1. Create a new project
2. View Projects
3. Add Task
4. Assign Task
5. View Project Tasks
6. Update Task Status
7. Track Project Progress
8. Search Projects
9. Identify Overdue Tasks
10. Generate Project Report
11. Exit
```

## Data Structure

Projects are stored in a dictionary indexed by project ID. Each project contains its own details and a list of task dictionaries. This makes it possible to access a project directly by its ID and manage its tasks separately.

```python
Projects = {
    1001: {
        "Name": "AI Implementation",
        "Client": "ABC Consulting",
        "Project Manager": "Ahmed",
        "Start Date": "01/12/2026",
        "Deadline": "01/03/2027",
        "Status": "In Progress",
        "Tasks": [
            {
                "Task ID": 1,
                "Name": "Requirement Analysis",
                "Description": "Collect client requirements",
                "Assignee": "Ali",
                "Deadline": "15/12/2026",
                "Priority": "High",
                "Status": "In Progress"
            }
        ]
    }
}
```

## Sample Output

An illustrative project report for a project with five tasks, three of which are completed:

```text
Project Report for Project ID 1001:
Project ID: 1001
Project Name: AI Implementation
Client: ABC Consulting
Project Manager: Ahmed
Start Date: 01/12/2026
Deadline: 01/03/2027
Status: In Progress

Total Tasks: 5
Completed Tasks: 3
In Progress Tasks: 1
Pending Tasks: 1
Progress: 60.00%
Overdue Tasks: 0
```

Project completion is calculated as the number of completed tasks divided by the total number of tasks, multiplied by 100. Every task has equal weight.

## Project Structure

```text
03-business-project-management-system/
    main.py
    test_project_manager.py
    test-results.txt
    README.md
```

## How to Run

1. Download or clone the repository.
2. Open the `03-business-project-management-system` folder in VS Code or a terminal.
3. Run the application:

```bash
python main.py
```

Select a menu option from 1 to 11. Create a project before adding or assigning tasks. Enter dates in `DD/MM/YYYY` format.

## Testing

The application includes 18 automated tests covering project and task creation, ID generation, input validation, task assignment, status changes, progress calculations, search, overdue task detection, reporting and complete menu navigation.

All 18 tests passed on Python 3.13.5.

To run the tests:

```bash
python -m unittest -v
```

## What I Learned

My previous projects focused on managing customer accounts and analysing financial transactions. This project combines those concepts in a project management workflow.

I practised accessing and modifying nested dictionaries, storing tasks inside individual projects, searching for specific records and calculating progress from task statuses. Building the application also highlighted the importance of variable scope, indentation, connecting functions correctly and testing the complete program.

The project was developed as a guided learning exercise, with assistance for debugging, reusable validation functions and automated testing.

## Current Limitations

- Projects and tasks are stored in memory and are lost when the application closes.
- All tasks have equal weight when calculating progress.
- Task deadlines are not restricted to the associated project's date range.
- Team members are entered manually; there is no separate user database or authentication.
- Reports are displayed in the terminal rather than exported.
- Projects and tasks cannot currently be deleted.

## Future Improvements

- Permanent storage using SQLite or JSON.
- Employee management and role-based access.
- Project and task editing, deletion and archiving.
- Weighted progress tracking and milestone management.
- Automated deadline reminders.
- Excel or PDF report exports.
- A web-based dashboard for project monitoring.
- AI-assisted project reporting and risk identification.

## Author

Izaan Mian

Project 03 — Python Portfolio
