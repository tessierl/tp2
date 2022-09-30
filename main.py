#Programme fait par Lucas Tessier
#Groupe 402
#Programme où l'ordi choisit un nombre aléatoire entre 0 et 100 et le joueur doit deviner en un nombre d'essais indéfini le nombre

import random

boucle_jeu = True
while boucle_jeu:   #boucle de tout le jeu quand on veut recommencer
    nb_essai = 0
    tours = True
    ordi = random.randint(0, 100)   #le nombre est caractérisée par ordi
    print("J’ai choisi un nombre au hasard entre 0 et 100. À vous de le deviner...")
    while tours:    #boucle pour les essais
        essai = int(input("Entrez votre essai :"))
        if essai > ordi :
            print("Mauvais choix, le nombre que j'ai choisi est plus petit.")
            nb_essai += 1   #on oubli pas d'ajouter un essai dans nb_essai
        elif essai < ordi :
            print("Mauvais choix, le nombre que j'ai choisi est plus grand.")
            nb_essai += 1
        elif essai == ordi :
            nb_essai += 1
            string = """
        $$$$
       $$__$
       $___$$
       $$___$$
        $____$$
        $$____$$$
         $$_____$$
         $$______$$
          $_______$$
    $$$$$$$________$$
  $$$_______________$$$$$$
 $$____$$$$____________$$$
 $___$$$__$$$____________$$
 $$________$$$____________$
  $$____$$$$$$____________$
  $$$$$$$____$$___________$
  $$_______$$$$___________$
   $$$$$$$$$__$$_________$$
    $________$$$$_____$$$$
    $$____$$$$$$____$$$$$$
     $$$$$$____$$__$$
       $_____$$$_$$$
        $$$$$$$$$$"""
            print(string)   #petite illustration pour te féliciter :)
            print(f"Bravo! Bonne réponse! Vous avez réussi en {nb_essai} essais")
            quit = input("Voulez-vous recommencer (y/n)?")
            tours = False
            if quit == "n":
                print("Merci d'avoir joué! :)")
                boucle_jeu = False  #fin du programme