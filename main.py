#Programme fait par Lucas Tessier
#Groupe 402
#


import random

ordi = random.randint(0, 100)
nb_essai = 0

print("J’ai choisi un nombre au hasard entre borne_minimale et borne_maximale. À vous de le deviner...")
essai = input("Entrez votre essai :")

if essai < ordi :
    print("Mauvais choix, le nombre que j'ai choisi est plus petit.")
    essai
    nb_essai =+1
