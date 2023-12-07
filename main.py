# main.py

from clear_screen import clear_screen, wait_and_clear_screen
from welcome_gui import welcome
from menu_info import menu
from task import Task
from tasklist import Tasklist

FILENAME = 'data.csv'

def linebreak():
    print('\n\n')

def add_task(tasklist):
    task = Task(
        task_name=input('Enter the task name you want to add: '),
        task_desc=input('Enter the task description if any: ')
    )
    tasklist.add_task(task)

def remove_task(Tasklist):
    task_id = int(input('Enter the task_id you want to remove: '))
    Tasklist.remove_task(task_id)

def display_tasks(Tasklist):
    Tasklist.display_tasks()

def update_task(Tasklist, task_id):
    Tasklist.update_task(task_id, True)

def main():
    # early preparations
    tasklist = Tasklist()
    tasklist.import_from_csv(FILENAME)

    # starting the home page
    clear_screen()
    welcome(80)

    while 1:
        wait_and_clear_screen()
        menu(80)
        linebreak()
        prompt = int(input("Enter your choice : "))
        if prompt == 0 : break
        if prompt == 1 :
            # add task here
            add_task(tasklist)
            #tasklist.display_tasks()
            continue
        if prompt == 2 :
            # remove task here
            remove_task(tasklist)
            continue
        if prompt == 3 : 
            # show tasks here
            display_tasks(tasklist)
            #wait_and_clear_screen()
            continue
        if prompt == 4 :
            # update task here
            task_id=int(input("Enter task ID - "))
            update_task(tasklist, task_id)
            continue
        else :
            print('Invalid input!!\n')
            print('Please enter a valid option from menu!\n')

    tasklist.export_to_csv(FILENAME)
    clear_screen()
    print('Thankyou for using this app.\n')
    print('Have a nice day :)')

# calling the main function
main()