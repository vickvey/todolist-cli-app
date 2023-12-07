# defining menu
def menu(x):
    x=int(x/3)
    # x gives no of spaces
    print(" "*x ,"     Menu-options are")
    print("*"*3*x)
    print(" "*x ,"1. Add Task")
    print(" "*x ,"2. Remove Task")
    print(" "*x ,"3. Show Task")
    print(" "*x ,"4. Mark a Task done")
    print(" "*x ,"Press 0 to exit the program")
    print("*"*3*x)