print("You take three steps away from the ladder, when you notice a glimmer in the shadows. You fear it is a monster. ")
print("You attempt to draw your sword, only to find nothing. It must have been pickpocketed by a monster while you ")
l = input("were unlocking the door. Do you investigate the glimmer, even if you are weaponless? (y/n)")
if l == "y":
    print("You cautiously walk towards the glimmer, only to find a long chain, with a fancy spear head adorned on the")
    print("tip. Nice score!")
else:
    print("You ignore the glimmer and move towards the artifact, along a long, thin bridge. You grab it! Mission")
    print("successful! Then, the catacomb is illuminated by a hundred torches. You look down. There are")
    print("massive jagged spikes awaiting you should you falloff the bridge. The spikes are adorned by countless heads")
    print("of adventurers who came here before you. Then, a masked, cloaked figure drops from the ceiling onto the")
    print("bridge. Since you are weaponless, he easily swipes you off the bridge. Before your head can be")
    print("impaled by the jagged spikes, you wish you were a little bit more gutsy, as maybe the")
    print("thing glimmering in the shadows may have helped you in this situation. You are then impaled.")
    print("Game Over!")
    exit()
k = input("You see the artifact along a long, thin bridge. Do you walk towards the artifact? (y/n)")
if k == "y":
    print("You walk slong the bridge and grab the artifact. Nice! The artifact is shaped like a fan, with blades ")
    print("clipped onto it. You turn around to leave, only for the catacomb to be illuminated by many, many torches")
    print("Then, you notice that the bridge is surrounded by a massive drop, which, at the bottom has millions of")
    print("jagged spikes, all adorned with one or two human heads. Then, a masked, cloaked figure drops from ")
    print("the ceiling onto the bridge. He pulls out a pair of sai and doesn't look friendly. The artifact")
    print("also looks like a weapon you could use, but since you need to bring it back to the king, you can't")
else:
    print("You do not trust anything in the catacomb, and turn to leave, even if the king punishes you for")
    print("chickening out. However, when you climb back up the ladder, you find that the door is locked.")
    print("Then, the catacomb lights up, revealing many, many spikes at the bottom. You try all you can to,")
    print("open the door, try attacking it with the chain-spear, kicking it, using the key, nothing works.")
    print("You are stuck in the catacomb for the rest of your days. You last a few weeks before")
    print("becoming extremely weak due to starvation. You consider going towards the artifact, but you cannot bring")
    print("yourself to do it. In your last moments you make a dash for the artifact for a possible escape. ")
    print("However, in your weak state, you lose your foting and fall off the bridge towards the spikes. ")
    print("Before you are impaled, you wish you weren't as cowardly as you were today. You are then impaled. ")
    print("Game Over! ")
    exit()
e = input("use it as a weapon. You do have the chain-spear. Use it? (y/n)")
if e == "y":
    exit() #create use weapon scenario, remove exit