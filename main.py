
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


print('Hello '+name+".")
print("What pronouns shall your character follow?")
yn=""
pronouns = ""
while pronouns!= "m" and pronouns!= "f" and pronouns!= "n":
    pronouns = input("(m)ale (f)emale (n)on-binary:")
    if pronouns!= "m" and pronouns!= "f" and pronouns!= "n":
        
        print("Sorry I cannot define that. Please select from the availible choices")
        pronouns = ""
        pronouns = input("(m)ale (f)emale (n)on-binary:")
    else :
        if pronouns == "m":
            print("You have chosen to be Male. Are you satisfied with this choice?")
            yn= input("y/n")
            if yn != "y" and yn != "n" :
                yn= input("y/n:")
            else: 
                if yn == "y":
                    pronouns="m"
                    break
                else:
                    yn=""
                    pronouns=""
        if pronouns == "f":
            print("You have chosen to be Female. Are you satisfied with this choice?")
            yn= input("y/n:")
            if yn != "y" and yn != "n" :
                yn= input("y/n:")
            else: 
                if yn == "y":
                    pronouns="f"
                    break
                else:
                    yn=""
                    pronouns=""
        if pronouns == "n":
            print("You have chosen to be Non-Binary. Are you satisfied with this choice?")
            yn= input("y/n:")
            if yn != "y" and yn != "n" :
                yn= input("y/n:")
            else: 
                if yn == "y":
                    pronouns="n"
                    break
                else:
                    yn=""
                    pronouns=""
                    
                    
print(chr(27) + "[2J")
print(chr(27) + "[2J")
print("You are "+name+".")
if pronouns=="m":
    print("You are a male individual.")
if pronouns=="f":
    print("You are a female individual.")
if pronouns=="n":
    print("You are a non-binary individual.")
print(chr(27) + "[2J")

input("Hit enter to begin")

print(chr(27) + "[2J")


print("You wake up on the cold hard floor. You get up to see you've been transported to a dungeon. You hear water dripping.")

print("There is a door but it seems to be locked.")
print("There may be a key nearby.")
print(chr(27) + "[2J")
act = input("What will you do? type "help" for commands.")
if act == "help":
    print"