key = "unobtained"
s = input("pick up key? (y/n)")
if s == "y":
    key = "obtained"
    print("You picked up the key!")
u = input("Open hatch? (y/n)")
if u == "y" and key == "obtained":
    print("You opened the hatch! ")
else:
    print("You don't have the key. Dumbass. ")
