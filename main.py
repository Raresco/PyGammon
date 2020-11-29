import pygame

# Initalizare pygame
pygame.init()

# Initializare ecran
HEIGHT = 800
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))


def main_menu():

    # menu buttons:

    human_vs_human = pygame.image.load("images/hvh1.png")
    human_vs_human_toggled = pygame.image.load("images/hvh2.png")
    human_vs_human_pressed = pygame.image.load("images/hvh3.png")

    human_vs_ai = pygame.image.load("images/hva1.png")
    human_vs_ai_toggled = pygame.image.load("images/hva2.png")
    human_vs_ai_pressed = pygame.image.load("images/hva3.png")

    button1 = human_vs_human
    button2 = human_vs_ai
    clock = pygame.time.Clock()
    clock.tick(60)

    while True:
        bp = 0
        button1 = human_vs_human
        button2 = human_vs_ai

        display_menu_background()
        if 305 < pygame.mouse.get_pos()[0] < (305 + human_vs_human.get_width()) and 200 < pygame.mouse.get_pos()[1] < 245:
            button1 = human_vs_human_toggled

        if 328 < pygame.mouse.get_pos()[0] < 328 + human_vs_ai.get_width() and 300 < pygame.mouse.get_pos()[1] < 345:
            button2 = human_vs_ai_toggled

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and button1 == human_vs_human_toggled:
                button1 = human_vs_human_pressed
                bp = 1

            elif event.type == pygame.MOUSEBUTTONDOWN and button2 == human_vs_ai_toggled:
                button2 = human_vs_ai_pressed
                bp = 1

        screen.blit(button1, (305, 200))
        screen.blit(button2, (328, 300))

        pygame.display.update()
        if bp == 1:
            pygame.time.wait(150)

def display_menu_background():
    screen.blit(menu_background, (backgroundX, backgroundY))
    screen.blit(logo, (300, 25))


# Titlu si Iconita
pygame.display.set_caption("PyGammon")
icon = pygame.image.load('images/backgammon.png')
pygame.display.set_icon(icon)

# Menu Background
menu_background = pygame.image.load('images/menu.png')
logo = pygame.image.load('images/logo.png')
backgroundX = 0
backgroundY = 0

# Game Loop
main_menu()

