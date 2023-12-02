import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_enter():
    input("Press Enter to continue...")
    clear_screen()

def clear():
    wait_for_enter()
    clear_screen()

# Example usage:
'''clear_screen()
print("Screen 1 content")
wait_for_enter()
clear_screen()
print("Screen 2 content")
wait_for_enter()''' 

