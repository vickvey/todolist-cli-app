import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_enter():
    input("Press Enter to continue...")
    clear_screen()

def wait_and_clear_screen():
    wait_for_enter()
    clear_screen()


