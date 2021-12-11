from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time =", current_time)
key = "unobtained"
s = input("Pick up key? (y/n)")
if s == "y":
    key = "obtained"
    print("You picked up the key!")
else:
    print("This key's required, so I don't know why you aren't picking it up. ")
u = input("Open hatch? (y/n)")
if u == "y" and key == "obtained":
    print("You opened the hatch! ")
    m = input("")
if u == "n" and key == "obtained":
    print("You have the key, but you don't want to open the thing the key goes into? Why are you playing this?")
    print("Game Over!")
    exit()
else:
    print("You don't have the key. Dumbass. ")
