"""A terminal-based project and task management system."""

from datetime import date, datetime

Projects = {}


def read_id(prompt):
    """Read a positive integer ID, or return None for invalid input."""
    value = input(prompt).strip()
    try:
        number = int(value)
        if number > 0:
            return number
    except ValueError:
        pass
    print("Invalid ID. Please enter a positive whole number.")
    return None


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return datetime.strptime(value, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Invalid date. Use DD/MM/YYYY.")


def select_project(prompt):
    Project_ID = read_id(prompt)
    if Project_ID is None:
        return None
    if Project_ID not in Projects:
        print("Project not found.")
        return None
    return Project_ID


def select_task(Project_ID):
    Task_ID = read_id("Enter the Task ID: ")
    if Task_ID is None:
        return None
    for task in Projects[Project_ID]["Tasks"]:
        if task["Task ID"] == Task_ID:
            return task
    print("Task not found.")
    return None


def update_project_status(Project_ID):
    """Keep the project status consistent with its task statuses."""
    tasks = Projects[Project_ID]["Tasks"]
    completed = 0
    started = 0
    for task in tasks:
        if task["Status"] == "Completed":
            completed += 1
        if task["Status"] in ["In Progress", "Completed"]:
            started += 1
    if tasks and completed == len(tasks):
        status = "Completed"
    elif started > 0:
        status = "In Progress"
    else:
        status = "Not Started"
    Projects[Project_ID]["Status"] = status


def create_project():
    project_name = read_text("Enter Your Project Name: ")
    Client = read_text("Enter the Name of the Client: ")
    Project_Manager = read_text("Enter the Name of the Project Manager: ")
    Start_Date = read_date("Enter the Start Date (DD/MM/YYYY): ")
    while True:
        Deadline = read_date("Enter the Deadline (DD/MM/YYYY): ")
        if datetime.strptime(Deadline, "%d/%m/%Y") >= datetime.strptime(Start_Date, "%d/%m/%Y"):
            break
        print("Project deadline cannot be before its start date.")

    Project_ID = len(Projects) + 1001
    Project = {
        "Name": project_name,
        "Client": Client,
        "Project Manager": Project_Manager,
        "Start Date": Start_Date,
        "Deadline": Deadline,
        "Status": "Not Started",
        "Tasks": []
    }
    Projects[Project_ID] = Project
    print("Project created successfully!")
    print(f"Project ID: {Project_ID}")


def print_project(Project_ID, Project):
    print(f"Project ID: {Project_ID}")
    print(f"Project Name: {Project['Name']}")
    print(f"Client: {Project['Client']}")
    print(f"Project Manager: {Project['Project Manager']}")
    print(f"Start Date: {Project['Start Date']}")
    print(f"Deadline: {Project['Deadline']}")
    print(f"Status: {Project['Status']}")
    print()


def view_projects():
    if len(Projects) == 0:
        print("No projects found.")
        return
    for Project_ID, Project in Projects.items():
        print_project(Project_ID, Project)


def add_task():
    Project_ID = select_project("Enter the Project ID to add a task: ")
    if Project_ID is None:
        return
    task_name = read_text("Enter the Task Name: ")
    task_description = read_text("Enter the Task Description: ")
    task_deadline = read_date("Enter the Task Deadline (DD/MM/YYYY): ")
    while True:
        task_priority = input("Enter the Priority (High/Medium/Low): ").strip().title()
        if task_priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority.")
    Task_ID = len(Projects[Project_ID]["Tasks"]) + 1
    task = {
        "Task ID": Task_ID,
        "Name": task_name,
        "Description": task_description,
        "Assignee": "Unassigned",
        "Deadline": task_deadline,
        "Priority": task_priority,
        "Status": "Pending"
    }
    Projects[Project_ID]["Tasks"].append(task)
    update_project_status(Project_ID)
    print("Task added successfully.")
    print(f"Task ID: {Task_ID}")


def assign_task():
    Project_ID = select_project("Enter the Project ID to assign a task: ")
    if Project_ID is None:
        return
    task = select_task(Project_ID)
    if task is None:
        return
    assignee = read_text("Enter the name of the assignee: ")
    task["Assignee"] = assignee
    print(f"Task {task['Task ID']} assigned to {assignee}.")


def print_task(task):
    print(f"Task ID: {task['Task ID']}")
    print(f"Name: {task['Name']}")
    print(f"Description: {task['Description']}")
    print(f"Assignee: {task['Assignee']}")
    print(f"Deadline: {task['Deadline']}")
    print(f"Priority: {task['Priority']}")
    print(f"Status: {task['Status']}")
    print()


def view_project_tasks():
    Project_ID = select_project("Enter the Project ID to View Tasks: ")
    if Project_ID is None:
        return
    tasks = Projects[Project_ID]["Tasks"]
    if len(tasks) == 0:
        print("No tasks found for this project.")
        return
    print(f"Tasks for Project ID {Project_ID}:")
    for task in tasks:
        print_task(task)


def update_task_status():
    Project_ID = select_project("Enter the Project ID to update task status: ")
    if Project_ID is None:
        return
    task = select_task(Project_ID)
    if task is None:
        return
    new_status = input("Enter the new status (Pending/In Progress/Completed): ").strip().title()
    if new_status not in ["Pending", "In Progress", "Completed"]:
        print("Invalid status.")
        return
    task["Status"] = new_status
    update_project_status(Project_ID)
    print(f"Task {task['Task ID']} status updated to {new_status}.")


def task_counts(tasks):
    completed = 0
    in_progress = 0
    pending = 0
    for task in tasks:
        if task["Status"] == "Completed":
            completed += 1
        elif task["Status"] == "In Progress":
            in_progress += 1
        elif task["Status"] == "Pending":
            pending += 1
    return completed, in_progress, pending


def track_project_progress():
    Project_ID = select_project("Enter the Project ID to track progress: ")
    if Project_ID is None:
        return
    tasks = Projects[Project_ID]["Tasks"]
    if len(tasks) == 0:
        print("No tasks found for this project.")
        return
    total_tasks = len(tasks)
    completed_tasks, in_progress, pending = task_counts(tasks)
    progress_percentage = (completed_tasks / total_tasks) * 100
    print(f"Project ID {Project_ID} Progress: {progress_percentage:.2f}% completed.")
    print(f"Status: {Projects[Project_ID]['Status']}")


def search_projects():
    search_term = read_text("Enter the project ID, name or client name to search: ").lower()
    found_projects = []
    for Project_ID, Project in Projects.items():
        if (search_term == str(Project_ID) or search_term in Project["Name"].lower()
                or search_term in Project["Client"].lower()):
            found_projects.append((Project_ID, Project))
    if found_projects:
        print("Found Projects:")
        for Project_ID, Project in found_projects:
            print_project(Project_ID, Project)
    else:
        print("No projects found matching the search criteria.")


def find_overdue_tasks(Project_ID=None, current_date=None):
    """Return unfinished tasks whose deadlines are before the reference date."""
    if current_date is None:
        current_date = date.today()
    overdue_tasks = []
    for pid, Project in Projects.items():
        if Project_ID is not None and pid != Project_ID:
            continue
        for task in Project["Tasks"]:
            task_deadline = datetime.strptime(task["Deadline"], "%d/%m/%Y").date()
            if task_deadline < current_date and task["Status"] != "Completed":
                overdue_tasks.append((pid, task))
    return overdue_tasks


def identify_overdue_tasks():
    overdue_tasks = find_overdue_tasks()
    if overdue_tasks:
        print("Overdue Tasks:")
        for Project_ID, task in overdue_tasks:
            print(f"Project ID: {Project_ID}")
            print_task(task)
    else:
        print("No overdue tasks found.")


def generate_project_report():
    Project_ID = select_project("Enter the Project ID to generate report: ")
    if Project_ID is None:
        return
    Project = Projects[Project_ID]
    tasks = Project["Tasks"]
    print(f"Project Report for Project ID {Project_ID}:")
    print_project(Project_ID, Project)
    completed, in_progress, pending = task_counts(tasks)
    progress = completed / len(tasks) * 100 if tasks else 0
    print(f"Total Tasks: {len(tasks)}")
    print(f"Completed Tasks: {completed}")
    print(f"In Progress Tasks: {in_progress}")
    print(f"Pending Tasks: {pending}")
    print(f"Progress: {progress:.2f}%")
    print(f"Overdue Tasks: {len(find_overdue_tasks(Project_ID))}")
    print()


def mainmenu():
    while True:
        print("\n====== Welcome to Project Management System ======")
        print("1. Create a new project")
        print("2. View Projects")
        print("3. Add Task")
        print("4. Assign Task")
        print("5. View Project Tasks")
        print("6. Update Task Status")
        print("7. Track Project Progress")
        print("8. Search Projects")
        print("9. Identify Overdue Tasks")
        print("10. Generate Project Report")
        print("11. Exit")
        Choice = input("Enter your Choice (1-11): ").strip()
        match Choice:
            case "1":
                create_project()
            case "2":
                view_projects()
            case "3":
                add_task()
            case "4":
                assign_task()
            case "5":
                view_project_tasks()
            case "6":
                update_task_status()
            case "7":
                track_project_progress()
            case "8":
                search_projects()
            case "9":
                identify_overdue_tasks()
            case "10":
                generate_project_report()
            case "11":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    mainmenu()
