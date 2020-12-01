import pygame
import random

pygame.init()  # Initalizare pygame

# Initializare ecran
HEIGHT = 800
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Title and Icon
pygame.display.set_caption("PyGammon")
icon = pygame.image.load('images/backgammon.png')
pygame.display.set_icon(icon)

# Menu Background
wood_texture = pygame.image.load("images/woodTexture.png")
board_image = pygame.image.load("images/board.png")
menu_background = pygame.image.load('images/menu.png')
logo = pygame.image.load('images/logo.png')

# PNG's for menu buttons :
human_vs_human = pygame.image.load("images/hvh1.png")
human_vs_human_toggled = pygame.image.load("images/hvh2.png")
human_vs_human_pressed = pygame.image.load("images/hvh3.png")
human_vs_ai = pygame.image.load("images/hva1.png")
human_vs_ai_toggled = pygame.image.load("images/hva2.png")
human_vs_ai_pressed = pygame.image.load("images/hva3.png")

# PNG's for dice
die_1 = pygame.image.load("images/dice_1.png")
die_2 = pygame.image.load("images/dice_2.png")
die_3 = pygame.image.load("images/dice_3.png")
die_4 = pygame.image.load("images/dice_4.png")
die_5 = pygame.image.load("images/dice_5.png")
die_6 = pygame.image.load("images/dice_6.png")


# WAV's for menu buttons
button_sound = pygame.mixer.Sound("sounds/button.wav")

# Initialize Clock
clock = pygame.time.Clock()
clock.tick(60)

# Initialize game_state
game_state = "menu1"

zaruri_png = {
    1: die_1,
    2: die_2,
    3: die_3,
    4: die_4,
    5: die_5,
    6: die_6
}

dice_rolled = (random.randint(1, 6), random.randint(1, 6))


def main_menu():
    global game_state, running
    button1 = human_vs_human
    button2 = human_vs_ai

    button_pressed = 0
    button1 = human_vs_human
    button2 = human_vs_ai

    # Highlight buttons on mouse-over
    display_menu_background()
    if 305 < pygame.mouse.get_pos()[0] < (305 + human_vs_human.get_width()) and 200 < pygame.mouse.get_pos()[1] < 245:
        button1 = human_vs_human_toggled

    if 328 < pygame.mouse.get_pos()[0] < 328 + human_vs_ai.get_width() and 300 < pygame.mouse.get_pos()[1] < 345:
        button2 = human_vs_ai_toggled

        # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and button1 == human_vs_human_toggled:
            button1 = human_vs_human_pressed
            button_pressed = 1
            game_state = "menu2"

        elif event.type == pygame.MOUSEBUTTONDOWN and button2 == human_vs_ai_toggled:
            button2 = human_vs_ai_pressed
            button_pressed = 1
            game_state = "menu2"

        # Set coordinates and type of buttons for next screen display
    screen.blit(button1, (305, 200))
    screen.blit(button2, (328, 300))
    pygame.display.update()

    if button_pressed == 1:
        pygame.mixer.Sound.play(button_sound)
        pygame.time.wait(150)


def display_menu_background():
    screen.blit(menu_background, (0, 0))
    screen.blit(logo, (300, 25))


def player_vs_player_menu():
    global running, dice_rolled
    display_menu_background()
    screen.blit(board_image, (199, 0))
    screen.blit(wood_texture, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_rolled = (random.randint(1, 6), random.randint(1, 6))
    screen.blit(zaruri_png[dice_rolled[0]], (20, 275))
    screen.blit(zaruri_png[dice_rolled[1]], (100, 275))


# Game Loop
running = True
while running:
    if game_state == "menu1":
        main_menu()
    elif game_state == "menu2":
        player_vs_player_menu()

    pygame.display.update()


