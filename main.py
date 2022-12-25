# import libraries
from enemies import *
from crosshair import *

# initialise pygame
pygame.init()

# create game window
pygame.display.set_caption('Castle Defender')
clock = pygame.time.Clock()
# load images
images = Images()
# create castle
castle = Castle()
#creat Crosshair
crosshair = Crosshair()

# enemy
# create groups
enemy_group = pygame.sprite.Group()
enemy = Enemies(enemy_health[0], enemy_animations[0], 190, SCREEN_HEIGHT - 150)
enemy_group.add(enemy)

# game loop
run = True
while run:
    clock.tick(FPS)
    # load Background
    images.run()
    # draw castle
    castle.run()
    # draw crosshair
    crosshair.draw()
    # draw enemy
    enemy_group.update(castle)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update.display.window
    pygame.display.update()

pygame.quit()
