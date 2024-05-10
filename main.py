
print("         ----------------------          ")
print("         Welcome to py-dungeon!          ")
print("         ----------------------          ")
print("                                         ")
print("Hit enter key to continue")
input()
print("What will you be known as?")
yn = False
ans=""
while yn == False:
    name= input("Name:")
    print("     ")
   
    while ans !="y":
        print("Do you want to be known as "+name+"? (y/n)")
        ans= input()
        if ans=="y":
            yn = True
            break
        else:
            yn= False
            break
    if yn == True:
        break
