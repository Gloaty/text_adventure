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
    print("After the king hears you declining, he is disgusted by your unwillingness to complete his mission. ")
    print("The king then executes you for disobeying his orders. You spend the last few days thinking about why the ")
    print("hell you turned down his mission. ")
    print("Game Over! ")
    exit()
o = input("The detour path goes near a waterfall connected to a lake. Do you head down the path? (y/n)")
if o == "y":
    print("You head down the path. Near the lake, you hear some of the most beautiful singing you have ever heard. ")
else:
    print("Since you see that the path is blocked, you return to the king and tell him that you could not complete the")
    print("mission due to the blockage. The king then points out the detour path. He then executes you for your ")
    print("stupidity. You spend your last few days wishing you spent more time listening in school. ")
    print("Game Over!")
    exit()
p = input("You have heard of the myths of the sirens, but never really believed them. Do you investigate? (y/n)")
if p == "n":
    print("You ignore the singing, and push forward towards the catacomb. You arrive at the graveyard, at which the ")
else:
    print("You go towards the singing emanating from the lake. All of a sudden, you are grabbed by a tentacle and ")
    print("taken under the water. Your last moment were spent thinking about the fact that you are seriously gullible.")
    print("You are never seen again. ")
    print("Game Over!")
    exit()
w = input("catacomb lies. You find the entrance to the catacomb. It is locked. Do you try to kick the door in? (y/n)")
if w == "n":
    print("Smart you! Instead of kicking it in, you search the nearby shed. You find the key on a shelf.")
else:
    print("Why did you kick it? You injured your foot doing that! How are you so prone to injury? Also, the door isn't")
    print("open. ")
    print("Then, a skeleton jumps you. You try to kick his skull off, but with your weakened foot, it barely gets up ")
    print("to his ribs. He then cuts your foot off. He walks off. You slowly bleed to death. Your last moments were ")
    print("spent wishing you had a little more brains than brawns. ")
    exit()
s = input("Pick up the key? (y/n)")
if s == "y":
    key = "obtained"
    print("You picked up the key. You return to the entrance")
else:
    print("This key's required, so I don't know why you aren't picking it up. ")
u = input("Open the door to the catacombs? (y/n)")
if u == "y" and key == "obtained":
    print("You opened the catacomb door! ")
    print("As you enter the door, you nearly fall as you fail to notice a ladder leading down to the catacomb. You ")
    print("look down the drop. ")
m = input("There is nothing but darkness in the catacomb. Do you climb down the ladder? (y/n)")
if m == "y":
    print("You sensibly go down the ladder, one rung at a time. Who's a genius? You are!")
else:
    print("As you try to turn around to leave, but the slippery floor of the catacomb entrance mans you fall ")
    print("backwards into the catacomb. The fall winds you. A monster in the shadows takes advantage of this, and ")
    print("decapitates you. ")
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
