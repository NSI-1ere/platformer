import os
import pyfiglet
import random

"""Pierre Feuille Ciseaux - Développé par Alaric REMY"""

def clear():
    """Fonction permettant de supprimer toutes les données présentes dans le terminal."""
    os.system("cls" if os.name == "nt" else "clear")

clear()

def printGameName():
    print(pyfiglet.figlet_format("PIERRE FEUILLE CISEAUX", font="digital"))

printGameName()

def playAgainst():
    print("\n[1] Jouer contre un robot\n[2] Joueur contre joueur\n")

    value = input("Choisissez le mode de jeu:\n> ")
    if value.isdigit() and (int(value) == 1 or int(value) == 2):
        return int(value)
    clear()
    print("Mode de jeu invalide, veuillez réessayer.")
    return playAgainst()

modeDeJeu = playAgainst()

def howManyPoints():
    print("\nCombien de manches souhaitez vous jouer ?\n")
    value = input("Choisissez le nombre de manches:\n> ")
    if value.isdigit():
        return int(value)
    clear()
    print("Nombre de manches invalide, veuillez réessayer.")
    return howManyPoints()

nombreDeManches = howManyPoints()

score = [0, 0]

nomJoueur = ""

if modeDeJeu == 2:
    nomJoueur = "Joueur 2"
else:
    nomJoueur = "Ordinateur"

for i in range(nombreDeManches):
    clear()

    dicoPierreFeuilleCiseaux = {
        "1": "Pierre",
        "2": "Feuille",
        "3": "Ciseaux"
    }

    def pierreFeuilleCiseaux(nbJoueur):
        printGameName()
        print(f"- Manche {i+1} -\n")
        print(f"Joueur 1 - {score[0]}\n{nomJoueur} - {score[1]}\n")
        print("[1] Pierre\n[2] Feuille\n[3] Ciseaux\n\n")
        value = input(f"[Joueur {nbJoueur}] Quel objet souhaitez vous jouer ?\n> ")
        if value.isdigit() and (value == "1" or value == "2" or value == "3"):
            clear()
            return value
        clear()
        print("\nObjet invalide, veuillez réessayer.\n")
        return pierreFeuilleCiseaux(nbJoueur)

    player1 = pierreFeuilleCiseaux("1")

    if modeDeJeu == "2":
        player2 = pierreFeuilleCiseaux("2")
    else:
        player2 = str(random.randint(1, 3))

    printGameName()
    print(f"Joueur 1 a joué {dicoPierreFeuilleCiseaux[player1]}")
    print(f"{nomJoueur} a joué {dicoPierreFeuilleCiseaux[player2]}")

    def logiquePierreFeuilleCiseaux(player1, player2):
        if player1 == player2:
            return [0, 0]
        if (player1 == "1" and player2 == "3") or (player1 == "2" and player2 == "1"):
            return [1, 0]
        if (player2 == "1" and player1 == "3") or (player2 == "2" and player1 == "1"):
            return [0, 1]
        
    resultat = logiquePierreFeuilleCiseaux(player1, player2)
    
    if resultat == [0, 0]:
        print("\nIl y a égalité !")
    elif resultat == [1, 0]:
        print("\nLe joueur 1 l'emporte !")
        score[0] += 1
    elif resultat == [0, 1]:
        if modeDeJeu == 2:
            print(f"\nLe joueur 2 l'emporte !")
        else:
            print("L'ordinateur l'emporte !")
        score[1] += 1
    
    
    wait = input("Appuyez sur entrée pour continuer..")

else: 
    clear()
    printGameName()
    print("Merci d'avoir joué !")
    if score[0]>score[1]:
        if modeDeJeu == 2:
            print(f"> Le joueur 1 l'emporte avec {score[0]} points contre le joueur 2 avec {score[1]} points !")
        else:
            print(f"> Le joueur 1 l'emporte avec {score[0]} points contre l'ordinateur avec {score[1]} points !")
    
    if score[1]>score[0]:
        if modeDeJeu == 2:
            print(f"> Le joueur 2 l'emporte avec {score[1]} points contre le joueur 1 avec {score[0]} points !")
        else:
            print(f"> L'ordinateur l'emporte avec {score[1]} points contre le joueur 1 avec {score[0]} points !")
    
    if score[0] == score[1]:
        print(f"Il y a eu égalité à {score[0]} points !")

    print("\n")

#Oui je peux opti mes "if mode de jeu tamère" est-ce que je veux ? non flemme mdrr
