import pygame
import random

pygame.init()  # Initalizare pygame


class Board:

    def __init__(self):
        self.board = [2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2]
        self.vector_selectii = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.piece_length = 45
        self.endgame_mov = False
        self.endgame_bej = False
        self.piese_stricate_bej = 0
        self.piese_stricate_mov = 0
        self.piese_afara_bej = 0
        self.piese_afara_mov = 0

    def display_from_vector(self):
        for i in range(len(self.vector_selectii)):
            if self.vector_selectii[i] == 1:
                if i < 12:
                    screen.blit(selection_current, (coordonate[i], 1))
                else:
                    screen.blit(selection_current, (coordonate[i], 594))

            if self.vector_selectii[i] == 2:
                if i < 12:
                    screen.blit(selection_available, (coordonate[i], 1))
                else:
                    screen.blit(selection_available, (coordonate[i], 594))

    def add_selected(self, coordonata, player):
        if (self.board[coordonata] ^ player) > 0 and self.board[coordonata] != 0:
            self.vector_selectii[coordonata] = 1

    def add_available(self, x, d1, d2, player):
        if self.type_of_move(x, d1, player) != 0 and self.board[x] != 0:
            self.vector_selectii[x+d1] = 2

        if self.type_of_move(x, d2, player) != 0 and self.board[x] != 0:
            self.vector_selectii[x + d2] = 2

        if self.type_of_move(x, d1 + d2, player) != 0 and self.board[x] != 0:
            self.vector_selectii[x + d1 + d2] = 2

    def reset(self):
        self.vector_selectii = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def type_of_move(self, x, die_value, player):

        if x + die_value > 23:
            return 0    # Invalid

        if (self.board[x] ^ player) > 0:
            if (self.board[x + die_value] ^ player) > 0:
                return 1    # Valid
            elif self.board[x + die_value] == 0:
                return 1    # Valid
            elif self.board[x + die_value] == -1 * player:
                return 2    # Valid + Take Piece
        return 0    # Invalid

    def make_move(self, x, y, player):
        if self.type_of_move(x, y, player) == 0:
            print("Invalid Move!")

    def change_board_state(self, board):
        self.board = board

    def draw_pieces(self, cordonate):
        temporary_board = self.board
        p1_piese_afara = font.render(str(self.piese_afara_bej), True, (255, 255, 255))
        p2_piese_afara = font.render(str(self.piese_afara_mov), True, (255, 255, 255))
        screen.blit(piesa_mov, (150, 50))
        screen.blit(piesa_bej, (150, 480))
        screen.blit(p1_piese_afara, (165, 60))
        screen.blit(p2_piese_afara, (165, 490))

        for i in range(len(temporary_board)):
            if temporary_board[i] > 0:
                nr_piese = temporary_board[i]
                if i < 12:
                    while nr_piese > 0:
                        screen.blit(piesa_bej, (cordonate[i], -30 + nr_piese * 45))
                        nr_piese -= 1
                else:
                    while nr_piese > 0:
                        screen.blit(piesa_bej, (cordonate[i], 585 - nr_piese * 45))
                        nr_piese -= 1

            if temporary_board[i] < 0:
                nr_piese = temporary_board[i]
                if i < 12:
                    while nr_piese < 0:
                        screen.blit(piesa_mov, (cordonate[i], -30 - nr_piese * 45))
                        nr_piese += 1
                else:
                    while nr_piese < 0:
                        screen.blit(piesa_mov, (cordonate[i], 585 - abs(nr_piese) * 45))
                        nr_piese += 1


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


class Moves():
    def __init__(self):
        self.vector_selectii = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def display_sss(self):
        for i in range(len(self.vector_selectii)):
            if self.vector_selectii[i] == 1:
                if i < 12:
                    screen.blit(selection_current, (coordonate[i], 1))
                else:
                    screen.blit(selection_current, (coordonate[i], 594))

    def add_selected(self, coordonata):
        self.vector_selectii[coordonata] = 1
        print(self.vector_selectii)

    def reset(self):
        self.vector_selectii = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def get_position(pos):
    x, y = pos
    print("pozitie = ", x, ", ", y)
    if 200 < x < 487:
        if y < 225:
            row = (x - 200) // 45
            return row
        elif y > 375:
            row = 23 - (x-200) // 45
            return row
    elif x > 520:
        if y < 225:
            row = (x - 235) // 45
            return row
        elif y > 375:
            row = 23 - (x-235) // 45
            return row


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
piesa_mov = pygame.image.load("images/piesa_mov.png")
piesa_bej = pygame.image.load("images/piesa_bej.png")
selection_available = pygame.image.load("images/available.png")
selection_current = pygame.image.load("images/selected.png")

# PNG's for dice
die_1 = pygame.image.load("images/dice_1.png")
die_2 = pygame.image.load("images/dice_2.png")
die_3 = pygame.image.load("images/dice_3.png")
die_4 = pygame.image.load("images/dice_4.png")
die_5 = pygame.image.load("images/dice_5.png")
die_6 = pygame.image.load("images/dice_6.png")

font = pygame.font.SysFont(None, 40)
p1_img = font.render('Player 1', True, (255, 213, 175))
p2_img = font.render('Player 2', True, (100, 48, 107))

# Initialize Clock
clock = pygame.time.Clock()
clock.tick(60)

# Initialize game_state
game_state = "menu1"

coordonate = {
    0: 214,
    1: 258,
    2: 304,
    3: 349,
    4: 394,
    5: 439,
    6: 515,
    7: 560,
    8: 605,
    9: 650,
    10: 695,
    11: 740,
    23: 214,
    22: 259,
    21: 304,
    20: 349,
    19: 394,
    18: 439,
    17: 515,
    16: 560,
    15: 605,
    14: 650,
    13: 695,
    12: 740,
}


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


def draw():
    display_menu_background()
    screen.blit(board_image, (199, 0))
    screen.blit(wood_texture, (0, 0))
    screen.blit(p2_img, (15, 20))
    screen.blit(p1_img, (15, 530))


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


diceRoll = 0
current_player = 1


def player_vs_player():
    global diceRoll, current_player
    global running, dice_rolled
    draw()
    tabla.draw_pieces(coordonate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Dice.play_dice_animation()
                dice_rolled = Dice.roll_dice()
                diceRoll = 1

    if diceRoll == 1:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected = get_position(pos)
            if selected is not None:
                tabla.reset()
                tabla.add_selected(selected, current_player)
                tabla.add_available(selected, dice_rolled[0], dice_rolled[1], current_player)

    tabla.display_from_vector()
    screen.blit(zaruri_png[dice_rolled[0]], (20, 275))
    screen.blit(zaruri_png[dice_rolled[1]], (100, 275))

    pygame.display.update()


# Game Loop
running = True
tabla = Board()
tabla.__init__()
dice_rolled = Dice.roll_dice()

while running:
    if game_state == "menu1":
        main_menu()
    elif game_state == "menu2":
        player_vs_player()



