# lets make task structure
def linebreak() :
    print('\n\n')

class Task :
    def __init__ (self, task_name, task_desc, task_status = False) :
        self.task_id = self.get_next_task_id()
        self.task_name = task_name
        self.task_desc = task_desc
        self.task_status = task_status

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

    def update_status(self, new_status) : 
        self.task_status = new_status
    

    def display_task_details(self):
        print(f'Task ID: {self.task_id}')
        print(f'Task Name: {self.task_name}')
        print(f'Task Description: {self.task_desc}')
        print(f'Task Status: {"Done" if self.task_status else "Not Done"}')

# initialised three Task objects
task1 = Task('Brush your teeth', 'Brush karle bhai')
task2 = Task('Take a bath', 'Nahane jaa nahane')
task3 = Task('Get Dressed', 'Kapde pehen bhai achhe se')


print(task1.task_id)
task1.display_task_details()
linebreak()

print(task2.task_id)
task2.display_task_details()
linebreak()

print(task3.task_id)
task3.display_task_details()
linebreak()

