"""
Programme fait par Lucas Tessier
Groupe 402
Programme où le programme choisit un nombre aléatoire entre deux nombres que le joueur a choisit et le joueur
doit deviner en un nombre d'essais indéfini le nombre
"""
import random


def nombre():
    minimum = int(input("inscrivez un nombre :"))
    maximum = int(input("Inscrivez un nombre plus grand :"))
    return minimum, maximum


boucle_jeu = True
while boucle_jeu:
    nb_essai = 0
    tours = True
    minimum, maximum = nombre()
    ordi = random.randint(minimum, maximum)
    print("J’ai choisi un nombre au hasard entre 0 et 100. À vous de le deviner...")
    while tours:
        essai = int(input("Entrez votre essai :"))
        if essai > ordi:
            print("Mauvais choix, le nombre que j'ai choisi est plus petit.")
            nb_essai += 1
        elif essai < ordi:
            print("Mauvais choix, le nombre que j'ai choisi est plus grand.")
            nb_essai += 1
        elif essai == ordi:
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
            print(string)
            print(f"Bravo! Bonne réponse! Vous avez réussi en {nb_essai} essais")
            quitter = input("Voulez-vous recommencer (y/n)?")
            tours = False
            if quitter == "n":
                print("Merci d'avoir joué! :)")
                boucle_jeu = False
