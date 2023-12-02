# defining menu
def menu(x):
    x=int(x/3)
    # x gives no of spaces
    print(" "*x ,"     Menu-options are")
    print("*"*3*x)
    print(" "*x ," Press 1 to Add Task")
    print(" "*x ," Press 2 to Remove Task")
    print(" "*x ," Press 3 to Show Task")
    print(" "*x ," Press 4 to Mark a Task done")
    print(" "*x ," Press 0 to exit the program")
    print("*"*3*x)

menu(80)