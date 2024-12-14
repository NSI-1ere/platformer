# Jeu Platformer
##### Développé par Alaric REMY, Eliot BORDIER & Robin TEXIER.

## - Sommaire
* Launcher
    * Fonctionnement
    * Graphismes
* Jeu
    * Fonctionnement
        * Joueur
        * Platformes
        * Pièces
        * Fin du jeu
    * Graphismes

## - Launcher
*Le launcher permet au joueur d'être introduit au jeu avant de le lancer. Il permet donc également de démarrer le platformer.*

#### Fonctionnement
* Le launcher doit être présenté sous forme d'une fenêtre, s'ouvrant lorsque le fichier '`launcher.py`' est exécuté.
    * Utilisation de la librairie '`tkinter`' de Python.
* Celui-ci doit permettre de lancer le jeu, à l'aide d'un bouton '*Lancer*'.
    * Exécution de la commande '`python main.py`'.
        * Il faut faire attention à spécifier le bon chemin (path) du fichier main.
* Utilisation du clavier
    * En plus de l'utilisation de la souris pour cliquer sur le bouton '*Lancer*', le joueur doit avoir la possibilité de simplement appuyer sur '*ESPACE*' pour lancer le jeu.

#### Graphismes
* La fenêtre du launcher ne doit pas être en écran plein (Fullscreen), mais occuper un petit espace au milieu de l'écran
    * Utilisation d'une résolution de *1000\*373px*
* Implémentation d'un arrière plan animé (gif)
    * Implémentation d'une fonction permettant de lire les gifs, frame par frame (image par image)

## - Jeu
*Le jeu s'inspire des bases du jeu "Doodle Jump". En raison de la deadline, nous ne pouvons pas implémenter toutes ses fonctions. Il est initialisé à l'aide de la commande `py main.py`.*

#### Fonctionnement
* Joueur:
   * Le joueur peut se déplacer sur les axes *x* et *y* (Plan 2D). Il peut donc se déplacer et sauter.
      * Utilisation des touches flèche gauche, flèche droite et espace.
      * Il apparaît sur une platforme 'initale'. Elle ne change pas d'une partie à une autre.

* Les platformes:
   * Utilisation d'une platforme initiale. Déterminée à l'aide de la taille de l'écran. Elle se place donc toujours au centre, en bas de l'écran.
   * Les platformes suivantes sont générées aléatoirement, en fonction de la position de la platforme précédente, dans une intervalle accessible par le joueur (Par le saut et le mouvement de gauche à droite, ou de droite à gauche)
        * Nous devons faire en sorte que les platformes ne soient pas générées trop loin, ni trop près.
   * Initialement, en plus de la platforme dite 'initiale', 3 platformes sont générées aléatoirement.

* Pièces - *Afin de donner un 'but' au jeu, nous implémentons un système de pièces.*
  * Les pièces sont générées aléatoirement (50% de chance) sur les platformes
  * Les pièces sont récupérables si le joueur rentre en collision avec celles-ci. On incrémente simultanément un compteur de pièces récupérées.
  * Au bout d'un nombre, défini dans la configuration, de pièces récupérées, la partie est considérée comme gagnée.
 
* Fin du jeu
  * Si le joueur sort de l'écran, le jeu se termine. On affiche "Game Over!" sur l'écran, ainsi que le texte "Please press Enter to retry". 
     * Si la touche Entrée est pressée, nous relançons le jeu (Nouvelle partie), sans passer par le launcher.
  * Si le compteur de pièces excède la valeur 'nombre de pièces maximales' dans la configuration, on affiche "Game Won!" sur l'écran, ainsi qu'encore une fois, "Please press Enter to retry".

#### Graphismes

* Platformes
  * Les platformes sont représentées par un rectangle de couleur définie dans le code. Par défaut du bleu.

* Joueur
   * Le joueur est représenté par un sprite, pouvant se déplacer de gauche à droite.

* Pièces
   * Un compteur de pièces est présent en haut à droite de l'écran, précédé par le sprite d'une pièce.

* Arrière-plan
   * Une image animée (gif) est présente derrière les platformes, le compteur et le joueur.
  



