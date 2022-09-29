#Programme fait par Lucas Tessier
#Groupe 402
#


import random

boucle_jeu = True
tours = True
while boucle_jeu:
    ordi = random.randint(0, 100)
    nb_essai = 0

    print("J’ai choisi un nombre au hasard entre borne_minimale et borne_maximale. À vous de le deviner...")
    while tours:
        essai = int(input("Entrez votre essai :"))

        if essai > ordi :
            print("Mauvais choix, le nombre que j'ai choisi est plus petit.")
            nb_essai += 1
            tours = False
        elif essai < ordi :
            print("Mauvais choix, le nombre que j'ai choisi est plus grand.")
            nb_essai += 1
            tours = False
        elif essai == ordi :
            print("Bravo! Bonne réponse! Vous avez réussi en ")
            quit = input("Voulez-vous recommencer (y/n)?")