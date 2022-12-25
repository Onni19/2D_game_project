import pygame.sprite
from castle import *

# load enemies
enemy_animations = []
enemy_types = ['knight']
enemy_health = [75]

animation_types = ['walk', 'attack', 'death']

for enemy in enemy_types:
    # load animation
    animation_list = []
    for animation in animation_types:
        # reset temporary list of images
        temp_list = []
        # define number of frames
        for i in range(NUMBER_Of_FRAMES):
            img = pygame.image.load(images_path + f'enemies/{enemy}/{animation}/{i}.png').convert_alpha()
            img_width = img.get_width()
            img_height = img.get_height()
            img = pygame.transform.scale(img, (int(img_width * ENEMY_SIZE), int(img_height * ENEMY_SIZE)))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)


class Enemies(pygame.sprite.Sprite):
    def __init__(self, health, animation_list, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = ENEMY_SPEED
        self.health = health
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        self.last_attack = pygame.time.get_ticks()
        self.attack_cooldown = 1000  # 1000ms difference between two attacks

        # select starting image
        self.image = self.animation_list[self.action][self.frame_index]
        # self.rect = self.image.get_rect() # default size statement
        self.rect = pygame.Rect(0, 0, 70, 90)  # customise the rectangle size
        self.rect.center = (x, y)

    def update_animation(self):

        # update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed on current action update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset, back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1

            else:
                self.frame_index = 0

    def update_action(self, new_action):

        # if the new action is different to the previous one
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0
            self.new_time = pygame.time.get_ticks()

    def update(self, target):

        if self.alive:
            # collision with bullet
            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25
                # print('hit')

            # enemy has reached the castle-collision with castle
            if self.rect.right > target.rect.left:
                self.update_action(1)  # print('reached castle')
            # move enemy
            if self.action == 0:
                self.rect.x += self.speed  # update rectangle position
            # attack
            if self.action == 1:
                if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
                    target.health -= 25
                    if target.health <= 0:
                        target.health = 0
                    #print(target.health)
                    self.last_attack = pygame.time.get_ticks()

            # if heath has dropped to  zero
            if self.health <= 0:
                target.money += 100
                target.score += 100
                self.update_action(2)  # enemy death
                self.alive = False

        self.update_animation()

        # draw image rectangle image on screen
        pygame.draw.rect(screen, WHITE, self.rect, 1)
        screen.blit(self.image, (self.rect.x + 30, self.rect.y - 10))  # draw image on screen
