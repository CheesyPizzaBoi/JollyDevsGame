import pygame, sys, random
from characteranims_ import Player_walk
from pygame.locals import *

pygame.init()
display_width = 1444
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
menu = pygame.image.load('./Assets/Main Menu.png')
scene = pygame.image.load('./Assets/Main_Scene.png')
clock = pygame.time.Clock()


moving_character = pygame.sprite.Group()
player_movement = Player_walk(600, 400)
moving_character.add(player_movement)


def main_menu():
    while True:
        window.blit(menu, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(373, 304, 673, 100)
        if button_1.collidepoint ((mx, my)):
            if click:
                game()
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
    otherscene = pygame.Rect(350, 350, 100, 100)
    library = pygame.image.load('./Assets/Library.png')

    library_x = 550
    library_y = 200


    library_rect = pygame.Rect(library_x, library_y, 357, 357)
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
    list = []
    timer = 0
    while generating:
        keys = pygame.key.get_pressed()
        x = random.randint(0, 1444)
        y = random.randint(0, 800)
        book = pygame.Rect(x, y, 100, 100)
        timer += 1

        if timer == 50:
            list.append(book)
            timer = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_RIGHT]:
            player_movement.animate()

        if keys[pygame.K_LEFT]:
            player_movement.animate()

        window.fill((0, 0, 0))
        for x in range(len(list)):
            pygame.draw.rect(window, (255, 0, 0), list[x])
        moving_character.draw(window)
        moving_character.update(0.25)
        pygame.display.flip()
        clock.tick(60)

main_menu()
