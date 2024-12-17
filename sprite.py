import pygame, os

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacement du Joueur avec Image")

# Classe Joueur
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        # Charger une image pour le joueur
        self.image_path = self.chemin_repertoire + r"\Jump.png"
        self.image_jump = self.chemin_repertoire + r"\Jump.png"
        self.image_landed = self.chemin_repertoire + r"\Landed.png"
        self.image_left = self.chemin_repertoire + r"\Left.png"
        self.image_right = self.chemin_repertoire + r"\Right.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Redimensionner l'image (optionnel)
        self.image = pygame.transform.scale(self.image, (25, 25))  # Ajustez la taille selon vos besoins
        # Obtenir le rectangle de l'image
        self.rect = self.image.get_rect()

    def set_center(self, player_x, player_y):
        # Initialiser la position du joueur
        self.rect.center = (player_x, player_y)

    def active_sprite(self, touches, ground, player_x, player_y, width, height):
        # Déplacement basé sur les touches pressées
        self.rect.y = player_y
        self.rect.x = player_x
        if touches[pygame.K_SPACE]:
            if self.image_path != self.image_jump:
                self.image_path = self.image_jump
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
        if ground == True:
            if self.image_path != self.image_landed:
                self.image_path = self.image_landed
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
        if ground == True and touches[pygame.K_LEFT]:
            if self.image_path != self.image_left:
                self.image_path = self.image_left
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
        if ground == True and touches[pygame.K_RIGHT]:
            if self.image_path != self.image_right:
                self.image_path = self.image_right
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
