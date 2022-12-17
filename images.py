from settings import *


class Images():
    def __init__(self):
        # load images
        self.bg = pygame.image.load(images_folder_path + 'bg_4.png').convert_alpha()

    def run(self):
        # load bg in screen
        screen.blit(self.bg, (0, 0))
