import pygame, os

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacement du Joueur avec Image")

# Classe Joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        # Charger une image pour le joueur
        self.image_path = self.chemin_repertoire + r"\Jump.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Redimensionner l'image (optionnel)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajustez la taille selon vos besoins
        # Obtenir le rectangle de l'image
        self.rect = self.image.get_rect()
        # Initialiser la position du joueur
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        # Vitesse du joueur
        self.vitesse = 5

    def deplacer(self, touches):
        # Déplacement basé sur les touches pressées
        if touches[pygame.K_UP]:
            self.rect.y -= self.vitesse
            if self.image_path != r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Background.jpg":
                self.image_path = r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Background.jpg"
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
        if touches[pygame.K_DOWN]:
            self.rect.y += self.vitesse
            if self.image_path != r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Background.jpg":
                self.image_path = r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Background.jpg"
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
        if touches[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
            if self.image_path != r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Mega man.gif":
                self.image_path = r"C:\Users\Eliot BORDIER\Downloads\projet1-development\projet1-development\Platformer\Mega man.gif"
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
        if touches[pygame.K_RIGHT]:
            self.rect.x += self.vitesse

# Création d'une instance du joueur
joueur = Joueur()

# Groupe de sprites (facilite le rendu et les collisions)
tous_les_sprites = pygame.sprite.Group()
tous_les_sprites.add(joueur)

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérer les touches pressées
    touches = pygame.key.get_pressed()

    # Déplacer le joueur
    joueur.deplacer(touches)

    # Rafraîchir l'écran
    screen.fill((0, 0, 0))  # Noir
    tous_les_sprites.draw(screen)  # Dessiner tous les sprites
    pygame.display.flip()

    # Contrôler la fréquence d'images
    clock.tick(60)

pygame.quit()
