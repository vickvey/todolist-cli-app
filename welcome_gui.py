# defining welcome
def welcome(z):
    wlcm_msg="Welcome to your To-do list."
    x=(len(wlcm_msg))
    y=int((z-x)/2)

    print("*"*z,end='')  
    print("\n"*2," "*y ,wlcm_msg, " "*y, "\n"*2 , sep= '', end= '')
    print("*"*z)

#calling welcome
welcome(80)
    


