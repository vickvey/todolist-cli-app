import csv
from task import Task
# here lets define tasklist

class Tasklist:
    def __init__(self):
        # private member containing a list of tasks
        self._Tasks = []

    def add_task(self, Task):
        self._Tasks.append(Task)

    def remove_task(self, task_id):
        self._Tasks = [task for task in self._Tasks if task.task_id != task_id]

    def display_tasks(self):
        # Display details of all tasks in the task list
        for task in self._Tasks:
            task.display_task_details()

    def update_task(self, task_id, new_status):
        for task in self._Tasks:
            if task.task_id == task_id:
                task.update_status(new_status)
                break

    def export_to_csv(self, filename):
        # Export tasks to a CSV file
        with open(filename, 'w', newline='') as file:
            fieldnames = ['Task ID', 'Task Name', 'Task Description', 'Task Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the tasks
            for task in self._Tasks:
                writer.writerow(task.to_dict())

    def import_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)

                # Read each row and create Task objects
                for row in reader:
                    task = Task(
                        int(row['Task ID']),
                        row['Task Name'],
                        row['Task Description'],
                        True if row['Task Status'] == 'Done' else False
                    )
                    self.add_task(task)

        except FileNotFoundError:
            # If the file is not found, create a new one with a header
            with open(filename, 'w', newline='') as file:
                fieldnames = ['Task ID', 'Task Name', 'Task Description', 'Task Status']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()