import pygame

# game window
SCREEN_WIDTH = 1136
SCREEN_HEIGHT = 620

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

#
FPS = 60

# castle scale
SCALE = 0.30
BULLET_SIZE = 0.028
BULLET_SPEED_INITIAL = 10
GOOD_CASTLE_INITIAL_HEALTH = 1000

# enemy
ENEMY_SPEED = 10
NUMBER_Of_FRAMES = 20
ENEMY_SIZE = 0.30
ANIMATION_COOLDOWN = 100

# load image folder path
images_path = 'assets/images/'

# create bullet groups
bullet_group = pygame.sprite.Group()
