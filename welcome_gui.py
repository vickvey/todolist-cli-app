# defining welcome
def welcome():
    print("*"*50,end='\n\n')
    wlcm_msg="Welcome to your To-do list."
    x=int(len(wlcm_msg))
    y=20-x/2
    print(" "*y,wlcm_msg," "*y,sep='')
    print("\n\n")
    print("*"*50,end='\n\n')

# defining main function
def main():
    welcome()

# calling main
main()