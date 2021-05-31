import random
import time
print("                --------------Bienvenue à notre jeux de Pierre papier ciseau ---------\n\n")

pierre = '''

     ___________
----|    _______)       
         (________)
         (________)
         (_______)
----*_____(______)
'''
paper = '''
     
      _______
_ _ _|    ___)_________
            ___________)
            _____________)
             __________)
-----*______________)
'''
scissors = '''
    ___________
---|      _____)______
              _________)
          _______________)
          (______)
-----*___(____)    

 '''
Choix = int(
    input(" ---- tapez 1 pour Pierre 2 pour Papier et 3 pour siso---- \n"))
if Choix == 1:
    print("---Pierre---\n")
    print(pierre)
elif Choix == 2:
    print("---Papier---\n")
    print(paper)
elif Choix == 3:
    print("---Sciseau---\n")
    print(scissors)

print("______La Machine va maintenant jouer_______\n")

time.sleep(3)

Choix2 = random.randint(1, 3)

if Choix2 == 1:
    print("---Pierre---")
    print(pierre)
elif Choix2 == 2:
    print("---Papier---")
    print(paper)
elif Choix2 == 3:
    print("---Sciseau---")
    print(scissors)

if Choix2 == Choix:
    print("---Match Null---")
elif Choix == 1:
    if Choix2 == 3:
        print("---UTILISATEUR A GAGNé ----")
    else:
        print("---MACHINE A GAGNé ----")
elif Choix == 2:
    if Choix2 == 1:
        print("---UTILISATEUR A GAGNé---")
    else:
        print("---MACHINE A GAGNé ----")
elif Choix == 3:
    if Choix2 == 2:
        print("---UTILISATEUR A GAGNé---")
    else:
        print("---MACHINE A GAGNé ----")
