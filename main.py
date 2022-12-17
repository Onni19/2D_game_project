# import libraries
from images import *

# initialise pygame
pygame.init()

# create game window
pygame.display.set_caption('Castle Defender')
clock = pygame.time.Clock()
# load images
images = Images()


# game loop
run = True
while run:
    clock.tick(FPS)
    # load Background
    images.run()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update.display.window
    pygame.display.update()

pygame.quit()
