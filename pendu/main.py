import os
import pyfiglet

"""Programme réalisé par Alaric REMY dans son entièreté. Utilisation légère de Stack Overflow."""

def clear():
    """Fonction permettant de supprimer toutes les données présentes dans le terminal."""
    os.system("cls" if os.name == "nt" else "clear")

clear()

print(pyfiglet.figlet_format("PENDU", font='slant'))
print(
    "Le pendu est un jeu simple nécessitant au moins deux joueurs.\n"+
      "> Un joueur définit un mot\n"+
      "> Un autre joueur doit deviner les lettres composant ce mot\n"+
      "- Le joueur cherchant le mot a le droit à au maximum 8 erreurs, au delà, le jeu sera perdu.\n\n"
      )

def motInput():
    motDef = str(input("Veuillez entrer le mot à chercher:\n> ")) #Définition du mot
    if len(motDef) < 2:
        clear()
        print("\nMerci d'entrer un mot d'au moins 2 lettres.\n")
        return motInput()
    return motDef

mot = motInput()


clear() #Nous supprimons les données du terminal pour cacher le mot.


listeJeu = [] #Définition de la liste visible par le joueur

ended = False #Valeur permettant de continuer (False), ou non (True), le jeu.

for i in range(len(mot)): #Boucle permettant d'entrer la première lettre du mot dans listeJeu, ainsi que des '_' à la place de toutes les autres lettres.
    if i == 0:
        listeJeu.append(mot[0])
        continue
    listeJeu.append("_")
    
print(listeJeu)

nbErreurs = 0 #Définition de la variable permettant de calculer le nombre d'erreurs

while ended == False:
    lettre = str(input("Veuillez entrer une lettre:\n> ")) #Définition de la lettre à 'chercher' dans le mot

    if lettre in mot: #Cette fonction, et la boucle, permettent de remplacer, si la lettre est dans le mot, tous les '_' correspondant à cette lettre, par la lettre.
        for i in range(len(mot)):
            if lettre == mot[i]:
                listeJeu[i] = lettre
        clear() #Pour une meilleure lisibilité, nous supprimons les données du terminal.
        print(listeJeu)

    else:  #Si la lettre n'est pas présente dans le mot:
        nbErreurs+=1 #On ajoute 1 erreur au compteur
        clear() 

        print(f"Faux !\nLa lettre {lettre} n'est pas présente dans le mot.\nVous êtes désormais à {nbErreurs}/8 erreurs.") #On donne une 'alerte' au joueur.
        print(listeJeu)

        if nbErreurs > 8: #Si il y a plus de 8 erreurs, le pendu est perdu.
            clear()
            perduText = pyfiglet.figlet_format("PERDU!", font='slant') #Définition du texte ascii "PERDU!"
            print(f"{perduText}\nLe mot était '{mot}'\n\n") #Envoi du message dans la console
            ended = True

    if listeJeu == list(mot): #Si la liste de jeu actuelle correspond au mot initial
        ended = True #Fin du jeu
        clear() #On nettoie le terminal
        bravoText = pyfiglet.figlet_format("BRAVO!", font='slant') #Définition du texte ascii du mot "BRAVO!"
        print(f"{bravoText}\nVous avez résolu le pendu avec {nbErreurs} erreurs, le mot était: '{mot}'\n\n") #Envoi du message de succès dans la console.

