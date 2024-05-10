import keyboard
print("         ----------------------          ")
print("         Welcome to py-dungeon!          ")
print("         ----------------------          ")
print("                                         ")
print("Hit any key to continue")
keyboard.wait()
print("What will you be known as?")
yn = false
while yn == False:
    name= input("Name:")
    print("     ")
    ans=""
    while ans !="y" or ans !="n":
        print("Do you want to be known as "+name+"? (y/n)")
        if ans=="y":
            yn == True
            break
    if yn == True:
        break

