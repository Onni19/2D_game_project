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
