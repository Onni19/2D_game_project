import pygame.transform

from settings import *


class Images():

    def image_process(self, image, scale):
        self.image = pygame.image.load(image).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))

        return self.image

    def load_bg(self):
        # load images
        self.bg = pygame.image.load(images_path + 'bg_4.png').convert_alpha()
        screen.blit(self.bg, (0, 0))  # load bg in screen

    def run(self):
        self.load_bg()


