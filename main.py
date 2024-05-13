
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
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print(chr(27) + "[2J")

print('Hello '+name+".")
print("What pronouns shall your character follow?")
yn=""
pronouns = ""
while pronouns == "":
    pronouns = input("(m)ale (f)emale (n)on-binary")
    if pronouns!= "m" and pronouns!= "f" and pronouns!= "m":
        
        print("Sorry I cannot define that. Please select from the availible choices")
        pronouns = input("(m)ale (f)emale (n)on-binary")
    else :
        if pronouns == "m":
            print("You have chosen to be Male. Are you satisfied with this choice?")
            yn= input("y/n")
            if yn != y and yn != n :
                yn= input("y/n")
            else: 
                if yn == "y":
                    pronouns="m"
                    break
                else:
                    yn=""
                    pronouns=""
