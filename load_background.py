import pygame
from PIL import Image

class load_background:
    def load_gif(self, filename):
        self.image = Image.open(filename)
        self.frames = []

        try:
            while True:
                self.frame = self.image.copy()
                self.frame = self.frame.convert("RGBA")
                self.frame_data = self.frame.tobytes("raw", "RGBA")
                self.surface = pygame.image.fromstring(
                    self.frame_data, self.frame.size, "RGBA"
                )
                self.frames.append(self.surface)
                self.image.seek(self.image.tell() + 1)
        except EOFError:
            pass
        return self.frames
