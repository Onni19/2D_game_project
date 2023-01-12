from bullet import *

img = Images()
images = {"castle_100": images_path + 'castle/castle1_100.png',
          "castle_50": images_path + 'castle/castle1_50.png',
          "castle_25": images_path + 'castle/castle1_25.png'}


class Castle():
    def __init__(self):
        self.health = GOOD_CASTLE_INITIAL_HEALTH
        self.fired = False
        self.score = 0
        self.money = 0

        # for Good castle
        self.castle_img_100 = img.image_process(images['castle_100'], SCALE)
        self.rect = self.castle_img_100.get_rect()
        self.rect.x = SCREEN_WIDTH - 260
        self.rect.y = SCREEN_HEIGHT - 400

    def load_images(self):

        self.castle_img_50 = img.image_process(images['castle_50'], SCALE)
        self.castle_img_25 = img.image_process(images['castle_25'], SCALE)

        # for bad Castle
        bad_castle_img = images_path + 'castle/bad100.png'
        self.bad_castle = img.image_process(bad_castle_img, SCALE)

    def draw(self):
        if self.health <= 250:
            self.castle_img = self.castle_img_25
        elif self.health <= 500:
            self.castle_img = self.castle_img_50
                    
                    
                    
                    from bullet import *

img = Images()
images = {"castle_100": images_path + 'castle/castle1_100.png',
          "castle_50": images_path + 'castle/castle1_50.png',
          "castle_25": images_path + 'castle/castle1_25.png'}


class Castle():
    def __init__(self):
        self.health = GOOD_CASTLE_INITIAL_HEALTH
        self.fired = False
        self.score = 0
        self.money = 0

        # for Good castle
        self.castle_img_100 = img.image_process(images['castle_100'], SCALE)
        self.rect = self.castle_img_100.get_rect()
        self.rect.x = SCREEN_WIDTH - 260
        self.rect.y = SCREEN_HEIGHT - 400

    def load_images(self):

        self.castle_img_50 = img.image_process(images['castle_50'], SCALE)
        self.castle_img_25 = img.image_process(images['castle_25'], SCALE)

        # for bad Castle
        bad_castle_img = images_path + 'castle/bad100.png'
        self.bad_castle = img.image_process(bad_castle_img, SCALE)

    def draw(self):
        if self.health <= 250:
            self.castle_img = self.castle_img_25
        elif self.health <= 500:
            self.castle_img = self.castle_img_50
        else:
            self.castle_img = self.castle_img_100

        screen.blit(self.castle_img, self.rect)
        screen.blit(self.bad_castle, (-230, SCREEN_HEIGHT - 465))

    def shoot(self):
        mouse_pos = pygame.mouse.get_pos()
        x_distance = mouse_pos[0] - self.rect.midleft[0]
        y_distance = mouse_pos[1] - self.rect.midright[1]
        self.angle = math.degrees(math.atan2(y_distance, x_distance))

        # get mouse clicked
        if pygame.mouse.get_pressed()[0] and self.fired == False:
            self.fired = True
            bullet = Bullet(self.rect.midleft[0], self.rect.midright[1], self.angle)
            bullet_group.add(bullet)
        # pygame.draw.line(screen, WHITE, (self.rect.midleft[0], self.rect.midright[1]), mouse_pos)
        if pygame.mouse.get_pressed()[0] == False:
            self.fired = False

    def run(self):
        self.load_images()
        self.draw()
        self.shoot()
        bullet_group.update()
        bullet_group.draw(screen)
        # print(len(bullet_group))

towers = {"tower100": "images/castle/tower100.png", "tower50": "images/castle/tower50.png",
               "tower25": "images/castle/tower25.png"}
    images_tower = [pygame.image.load(towers["tower100"]).convert_alpha(),
              pygame.image.load(towers["tower50"]).convert_alpha(),
              pygame.image.load(towers["tower25"]).convert_alpha()]


class Tower(pygame.sprite.Sprite, Castle):
    def __init__(self, display, images, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        Castle.__init__(self,  display, images, x, y, scale)
        self.image = self.images[0]
        self.got_target = False
        self.angle = 0
        self.last_shot = pygame.time.get_ticks()

    def set_health(self, health):
        self.health = health

    def update(self, enemy_group, bullet_group, health):
        self.health = health
        self.got_target = False
        target_x = 0
        target_y = 0
        for e in enemy_group:
            if e.alive:
                target_x, target_y = e.rect.midbottom
                self.got_target = True
                break

        if self.got_target:
            #pygame.draw.line(self.display, (255, 255, 255), (self.rect.center[0], self.rect.center[1]),
                             #(target_x, target_y-30))
            x_dist = target_x - self.rect.center[0]
            y_dist = (target_y-30) - self.rect.center[1]
            self.angle = math.atan2(y_dist, x_dist)

            shot_cooldown = 1500
            if pygame.time.get_ticks() - self.last_shot > shot_cooldown:
                bullet_sound.play()
                self.last_shot = pygame.time.get_ticks()
                arrow = bullet.Bullet(self.rect.center[0], self.rect.center[1], self.angle)
                bullet_group.add(arrow)

        self.draw()

