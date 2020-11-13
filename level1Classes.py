import pygame, random

class randomGeneration(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('./Assets/Library_Book.png'))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [position_x, position_y]

    def randomxy(self):
        self.rect.topleft = [random.randint(0, 1444), random.randint(0, 800)]