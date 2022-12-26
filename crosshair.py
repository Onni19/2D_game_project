from images import *


class Crosshair:
    def __init__(self):
        image1 = images_path+'crosshair/crosshair-removebg-preview.png'
        image2 = images_path+'crosshair/hand.png'
        img = Images()
        self.image1 = img.image_process(image1, 0.05)
        self.image2 = img.image_process(image2, 0.4)
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

        # hide mouse
        pygame.mouse.set_visible(False)

    def draw(self, draw=False):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if draw:
            self.rect2.center = (mouse_x + 8, mouse_y + 8)
            screen.blit(self.image2, self.rect2)
        else:
            if mouse_y < 100:
                self.rect2.center = (mouse_x+8, mouse_y+8)
                screen.blit(self.image2, self.rect2)
            else:
                self.rect1.center = (mouse_x, mouse_y)
                screen.blit(self.image1, self.rect1)

    def __del__(self):
        pass
