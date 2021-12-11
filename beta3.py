from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
key = "unobtained"
print("Current time =", current_time)
n = input("Pick up key? (y/n)")
if n == "y":
    print("You picked up the key!")
else:
    print("This key's required, so I don't know why you aren't picking it up. ")
# I wanted to have the hatch only open when the key is in the players inventory, but I'm unsure as to how I would do it
# code after this comment is how you do it

s = input("pick up key? (y/n)")
if s == "y":
    key = "obtained"
    print("You picked up the key!")
u = input("Open hatch? (y/n)")
if u == "y" and key =="obtained":
    print("You opened the hatch! ")
else:
    print("You don't have the key. Dumbass. ")

# copied into version 2