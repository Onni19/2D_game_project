from bullet import *


class Castle():
    def __init__(self, scale=SCALE):
        self.max_health = GOOD_CASTLE_INITIAL_HEALTH
        self.fired = False
        self.score = 0
        self.money = 0
        # for Good castle
        image = pygame.image.load(images_folder_path + 'castle/castle_100.png').convert_alpha()
        x = SCREEN_WIDTH - 260
        y = SCREEN_HEIGHT - 450

        width = image.get_width()
        height = image.get_height()

        self.castle_img = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.castle_img.get_rect()
        self.rect.x = x
        self.rect.y = y

        # for bad Castle
        bad_castle_img = pygame.image.load(images_folder_path + 'castle/bad100.png').convert_alpha()
        self.bad_castle = pygame.transform.scale(bad_castle_img,
                                                 (int(bad_castle_img.get_width() * scale),
                                                  int(bad_castle_img.get_height() * scale)))
