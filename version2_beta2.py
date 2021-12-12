from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time =", current_time)
key = "unobtained"

print("The BackStory")
t = input("The king has a mission for you. It is to recover a great, lost artifact. Do you accept his mission? (y/n)")
if t == "y":
    print("You set out on this great mission on your horse. Along the path, your map says you have to go along a ")
    print("path to the left. However, the path has a fallen tree blocking the path. You will have to take a detour. ")
else:
    print("The king then executes you for declining his mission. You spend the last few days thinking about why the ")
    print("hell you turned down his mission. ")
    print("Game Over! ")
    exit()
o = input("The detour path goes near a waterfall connected to a lake. Do you head down the path? (y/n)")
if o == "y":
    print("You head down the path. Near the lake, you hear some of the most beautiful singing you have ever heard. ")
else:
    print("Since you see that the path is blocked, you return to the king and tell him that you could not complete the")
    print(" mission due to the blockage. The king then points out the detour path. He then executes you for your ")
    print("stupidity. You spend your last few days wishing you spent more time listening in school. ")
    print("Game Over!")
    exit()
p = input("You have heard of the myths of the sirens, but never really believed them. Do you investigate? (y/n)")

s = input("Pick up key? (y/n)")
if s == "y":
    key = "obtained"
    print("You picked up the key!")
else:
    print("This key's required, so I don't know why you aren't picking it up. ")
u = input("Open hatch? (y/n)")
if u == "y" and key == "obtained":
    print("You opened the hatch! ")
m = input("There is nothing but darkness in the catacomb. Do you climb down the ladder? (y/n)")
if m == "y":
    print("You sensibly go down the ladder, one rung at a time. Who's a genius? You are!")
else:
    print("You try to turn around, but the slippery floor of the catacomb entrance mans you fall backwards into the ")
    print("catacomb. The fall winds you. A monster in the shadows takes advantage of this, and decapitates you. ")
    print("FATALITY!")
    print("Monster Wins!")
    print("Game over! ")
    exit()
if u == "n" and key == "obtained":
    print("You have the key, but you don't want to open the thing the key goes into? Why are you playing this?")
    print("Game Over! ")
    exit()
else:
    print("You don't have the key. Dumbass. Get it next time. ")
    print("Game Over! ")
    exit()
