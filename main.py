import pygame, sys, random
from characteranims_ import Player_walk
from level1Classes import randomGeneration
from pygame.locals import *
pygame.init()
display_width = 1444
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
menu = pygame.image.load('./Assets/Main Menu.png')
scene = pygame.image.load('./Assets/Main_Scene.png')
clock = pygame.time.Clock()

moving_character = pygame.sprite.Group()
player_movement = Player_walk(50, 310)
moving_character.add(player_movement)


def main_menu():
    while True:
        window.blit(menu, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(373, 304, 673, 100)
        button_3 = pygame.Rect(368, 610, 673, 98)
        if button_1.collidepoint ((mx, my)):
            if click:
                game()
        if button_3.collidepoint ((mx, my)):
            if click:
                howToPlay()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
def game():
    running = True
    library = pygame.image.load('./Assets/Library_Building.png')
    library_x = 450
    library_y = 83
    library_rect = pygame.Rect(library_x, library_y, 476, 476)
    while running:
        rect = pygame.Rect(player_movement.rect.x + 80, player_movement.rect.y + 70, 106, 196)
        keys = pygame.key.get_pressed()
        if rect.colliderect(library_rect):
            if keys[pygame.K_z]:
                level_1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        if keys[pygame.K_RIGHT]:
            player_movement.animate()
        if keys[pygame.K_LEFT]:
            player_movement.animate()

        window.blit(scene, (0, 0))
        window.blit(library, (library_x, library_y))
        moving_character.draw(window)
        moving_character.update(0.25)
        pygame.display.flip()
        clock.tick(60)
def level_1():
    generating = True
    points = 0
    x = random.randint(50, 1400)
    y = random.randint(230, 750)
    timer = 0
    book_group = pygame.sprite.Group()
    book_class = randomGeneration(x, y)
    book_group.add(book_class)

    while generating:
        rect = pygame.Rect(player_movement.rect.x + 80, player_movement.rect.y + 70, 106, 196)
        library_scene = pygame.image.load('./Assets/Library_Scene.png')
        window.blit(library_scene, (0, 0))
        keys = pygame.key.get_pressed()
        timer -= 1
        if rect.colliderect(book_class.rect):
            timer = random.randint(0, 200)
            book_group.remove(book_class)
            book_class.rect.topleft = [-100, 100]
            points += 1

        if timer == 0:
            book_group.add(book_class)
            book_class.randomxy()

        if points == 15:
            player_movement.rect.x = 50
            player_movement.rect.y = 310
            game()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_RIGHT]:
            player_movement.animate()
        if keys[pygame.K_LEFT]:
            player_movement.animate()
        if keys[pygame.K_UP]:
            player_movement.velocityY = -8
            player_movement.rect.y += player_movement.velocityY
        if keys[pygame.K_DOWN]:
            player_movement.velocityY = 8
            player_movement.rect.y += player_movement.velocityY
        book_group.draw(window)
        moving_character.draw(window)
        moving_character.update(0.25)
        pygame.display.flip()
        clock.tick(60)



def howToPlay():
    directions = True
    howToPlay_Screen = pygame.image.load('./Assets/howToPlay_Screen.png')
    while directions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    directions = False

        window.fill((99, 209, 229))
        window.blit(howToPlay_Screen, (0, 0))
        pygame.display.update()

main_menu()