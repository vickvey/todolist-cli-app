# lets make task structure
class Task:
    def __init__(self, task_id=None, task_name=None, task_desc=None, task_status=False):
        if task_id is None:
            task_id = self.get_next_task_id()

        self.task_id = task_id
        self.task_name = task_name
        self.task_desc = task_desc
        self.task_status = bool(task_status)

    def update_status(self, new_status):
        self.task_status = new_status

    def display_task_details(self):
        print(f'Task ID: {self.task_id}')
        print(f'Task Name: {self.task_name}')
        print(f'Task Description: {self.task_desc}')
        print(f'Task Status: {"Done" if self.task_status else "Not Done"}',end='\n\n')

    def to_dict(self):
        return {
            'Task ID': self.task_id,
            'Task Name': self.task_name,
            'Task Description': self.task_desc,
            'Task Status': 'Done' if self.task_status else 'Not Done'
        }

    def get_next_task_id(self):
        try:
            with open('task_id.txt', 'r') as file:
                task_id = int(file.read().strip())
        except FileNotFoundError:
            # If the file is not found, start with task ID 1
            task_id = 1

        # Increment task ID and update the file
        with open('task_id.txt', 'w') as file:
            file.write(str(task_id + 1))

        return task_id

'''
# Example of creating a Task instance
task = Task(task_name='Brush your teeth', task_desc='No desc', task_status=False)
task.display_task_details()'''
