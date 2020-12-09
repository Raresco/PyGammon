import pygame
import random

pygame.init()  # Initalizare pygame


class Dice:
    @staticmethod
    def roll_dice():
        return random.randint(1, 6), random.randint(1, 6)

    @staticmethod
    def play_dice_animation():
        pygame.mixer.Sound.play(dice_sound)
        for i in range(0, 10):
            dice_roll = Dice.roll_dice()
            pygame.time.wait(20)
            screen.blit(zaruri_png[dice_roll[0]], (20, 275))
            screen.blit(zaruri_png[dice_roll[1]], (100, 275))
            pygame.display.update()

class Button:
    def __init__(self, x_coordinate, y_coordinate, image, image_toggled, image_pressed):
        self.button_state = 'normal'
        self.png = image
        self.png_toggled = image_toggled
        self.png_pressed = image_pressed
        self.x = x_coordinate
        self.y = y_coordinate
        self.width = image.get_size()[0]
        self.height = image.get_size()[1]

    def is_hovered_over(self):
        if self.x < pygame.mouse.get_pos()[0] < (self.x + self.width) and \
                self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
            self.button_state = 'hovered'
        else:
            self.button_state = 'normal'
            return True

    def is_pressed(self):
        if self.button_state == 'hovered':
            self.button_state = 'pressed'
            return True

    def display_button(self):
        if self.button_state == 'normal':
            screen.blit(self.png, (self.x, self.y))
        elif self.button_state == 'hovered':
            screen.blit(self.png_toggled, (self.x, self.y))
        elif self.button_state == 'pressed':
            screen.blit(self.png_pressed, (self.x, self.y))

    @staticmethod
    def play_sound():
        pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/button.wav"))
        pygame.time.wait(300)


dice_sound = pygame.mixer.Sound("sounds/dice_roll.wav")

# Initializare ecran
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

hvh_button = Button(305, 200, human_vs_human, human_vs_human_toggled, human_vs_human_pressed)
hva_button = Button(328, 300, human_vs_ai, human_vs_ai_toggled, human_vs_ai_pressed)

def display_menu_background():
    screen.blit(menu_background, (0, 0))
    screen.blit(logo, (300, 25))


def main_menu():
    global game_state, running

    # Highlight buttons on mouse-over
    display_menu_background()

    if hvh_button.is_hovered_over():
        pass

    if hva_button.is_hovered_over():
        pass

        # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if hvh_button.is_pressed():
                game_state = "menu2"
                Button.play_sound()

            elif hva_button.is_pressed():
                game_state = "menu2"
                Button.play_sound()

    hvh_button.display_button()
    hva_button.display_button()

    pygame.display.update()


def player_vs_player_menu(start):
    global running
    display_menu_background()
    screen.blit(board_image, (199, 0))
    screen.blit(wood_texture, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Dice.play_dice_animation()
                dice_rolled = Dice.roll_dice()
                start = True

    if start:
        screen.blit(zaruri_png[dice_rolled[0]], (20, 275))
        screen.blit(zaruri_png[dice_rolled[1]], (100, 275))
        pygame.display.update()


# Game Loop
running = True
while running:
    if game_state == "menu1":
        main_menu()
    elif game_state == "menu2":
        player_vs_player_menu(False)

    pygame.display.update()


