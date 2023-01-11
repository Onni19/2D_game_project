import math
from images import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)  # calling super class
        bullet_img = images_path + 'bullet-1.png'
        img = Images()
        self.image = img.image_process(bullet_img, BULLET_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)  # convert input angle into radius
        # self.angle = angle # convert input angle into radius
        self.speed = BULLET_SPEED_INITIAL
        # calculate the horizontal and vertical speed based on the angle
        self.change_x_pos_dx = math.cos(self.angle) * self.speed
        self.change_y_pos_dy = math.sin(self.angle) * self.speed

    def update(self) -> None:
        # move bullet
        self.rect.x += self.change_x_pos_dx
        self.rect.y += self.change_y_pos_dy

