import pygame

class Player_walk(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites2 = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_1.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_2.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_3.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_4.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_5.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_6.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_7.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_8.png'))
        self.sprites.append(pygame.image.load('./Assets/Character_Walk_Animation/walk_9.png'))

        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_1.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_2.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_3.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_4.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_5.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_6.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_7.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_8.png'))
        self.sprites2.append(pygame.image.load('./Assets/Character_Walk_Animation_Left/left_walk_9.png'))



        self.current_sprite = 0
        self.current_sprite2 = 0
        self.image = self.sprites[self.current_sprite]
        self.velocityX = 0
        self.velocityY = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]



    def animate(self):
        self.is_animating = True


    '''def moving(self):
        x = 400
        y = 400
        move = 40
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.topleft = [x + move, y]
            x += move
    '''


    def update(self, speed):
        self.velocityX = 0
        self.velocityY = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.velocityX = 8
            if self.is_animating == True:
                self.current_sprite += speed

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.is_animating = False

                self.image = self.sprites[int(self.current_sprite)]
        if keys[pygame.K_LEFT]:
            self.velocityX = -8
            if self.is_animating == True:
                self.current_sprite2 += speed

                if self.current_sprite2 >= len(self.sprites2):
                    self.current_sprite2 = 0
                    self.is_animating = False

                self.image = self.sprites2[int(self.current_sprite2)]

        if keys[pygame.K_UP]:
            self.velocityY = -8
        if keys[pygame.K_DOWN]:
            self.velocityY = 8
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY


