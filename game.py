import pygame
import sys
import os
import subprocess
import numpy as np
from games.tictactoe import TicTacToe
from games.othello import Othello
from games.connect4 import Connect4


WIDTH = 825
HEIGHT = 825

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game Hub")

clock = pygame.time.Clock()

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Background
image_path = os.path.join(BASE_DIR, "images/menu2.png")
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Music
music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
else:
    print("menu_music.mp3 not found!")

# Buttons
buttons = {
    "flappy_bird": pygame.Rect(83, 250, 660, 117),
    "othello": pygame.Rect(85, 370, 655, 117),
    "connect4": pygame.Rect(84, 495, 655, 115),
    "tictactoe": pygame.Rect(85, 615, 655, 115),
    "exit": pygame.Rect(83, 740, 660, 117),
}

glow_colors = {
    "flappy_bird": (0, 0, 255),
    "othello": (0, 255, 0),
    "connect4": (255, 255, 0),
    "tictactoe": (255, 100, 0),
    "exit": (255, 0, 0),
}


def draw_glow(screen, rect, color):
    glow_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    for i in range(6, 0, -2):
        inner_rect = glow_surface.get_rect().inflate(-i * 8, -i * 8)
        pygame.draw.rect(
            glow_surface,
            (*color, 35),
            inner_rect,
            border_radius=20
        )
    screen.blit(glow_surface, rect.topleft)


def run_file(filename):
    file_path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(file_path):
        print(f"{filename} not found!")
        return

    
    subprocess.run([sys.executable, file_path])


# Base Game Class
class Game:
    def __init__(self, current_player, player1, player2, row, col):
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((row, col))
        self.current_player = player1

    def switch(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_win(self):
        raise NotImplementedError("Subclasses must implement this method")



def main():
    running1=True #tells the status of this running process 
    while running1:# if true then runs 
        mouse_pos = pygame.mouse.get_pos()
        hovered = None
        pygame.display.set_caption("Just a few more games… no promises 🎮😉")

        for event in pygame.event.get():# sees which type of event has occured 
            if event.type == pygame.QUIT:# the red cross at the top 
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["exit"].collidepoint(pos):#Ofc clicking on exit is just end of the game 
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                elif buttons["tictactoe"].collidepoint(pos):
                    game=TicTacToe()#We call the constructor of the class TicTacToe like c=int() is also valid it means that c will be of class int and have the initial value = 0 like c=1 is same as c=int(1)
                    pygame.display.set_caption("Just a quiet game of Tic Tac Toe ⭕❌🎮")# This text will come at the top of the screen of the game 
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "TicTacToe.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("TicTacToe.mp3 not found!")
                    running=True#This is the status of this particular game 

                    while running:
                        a="idk"# name anything like will not chnage if no clicks of quit or play_again 
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type==pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                row = y//game.cellsize
                                col = x//game.cellsize

                                
                                if game.makemove(row, col):
                                    if game.checkwin():
                                        winner = game.current_player  # current player just won
                                        a=game.end_screen(screen, winner)
                                        running = False
                                    elif game.isdraw():
                                        a=game.end_screen(screen,"draw")
                                        running = False
                                    else:
                                        game.switch() 
                        if a== "quit":
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            else:
                                print("menu_music.mp3 not found!")
                            running1=False

                        if a== "playagain":
                            #code for leaderboard.sh
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            else:
                                print("menu_music.mp3 not found!")
                            running1=True

                        game.drawgrid(screen)
                        game.drawmarks(screen)
                        pygame.display.update()#Easy code :)

                elif buttons["connect4"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "Connect4.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("Connect4.mp3 not found!")

                    game = Connect4()
                    pygame.display.set_caption("Keeping it simple—connect 4 🔴🔵")
                    running = True

                    while running:
                        a = "idk3.0"
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                row = y // game.cellsize
                                col = x // game.cellsize

                                if game.makemove(row, col):
                                    if game.checkwin():
                                        winner = game.current_player  # current player just won
                                        a=game.end_screen(screen, winner)
                                        running = False
                                    elif game.isdraw():
                                        a=game.end_screen(screen,"draw")
                                        running = False
                                    else:
                                        game.switch() 
                            
                        if a == "quit":
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            running1 = False

                        if a == "playagain":
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            running1 = True

                        game.drawgrid(screen)
                        game.drawmarks(screen)
                        pygame.display.update()

                elif buttons["othello"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "Othello.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("Othello.mp3 not found!")

                    game = Othello()
                    pygame.display.set_caption("Othello ⚫⚪ :)")
                    running = True

                    while running:
                        a = "idk2.0"

        #  CHECK GAME END (both players stuck)
                        if (not game.valid_possible(game.player1) and not game.valid_possible(game.player2)):

                            black = np.sum(game.board == 1)
                            white = np.sum(game.board == 2)

                            if black > white:
                                winner = 1
                            elif white > black:
                                winner = 2
                            else:
                                winner = "draw"

                            a = game.end_screen(screen, winner)
                            running = False

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                row = y // game.cellsize
                                col = x // game.cellsize

                                if game.makemove(row, col):

                                    game.switch()

                    #  skip turn logic
                                    if not game.valid_possible(game.current_player):
                                        game.switch()

                        # check again → game over
                                        if not game.valid_possible(game.current_player):

                                            black = np.sum(game.board == 1)
                                            white = np.sum(game.board == 2)

                                            if black > white:
                                                winner = 1
                                            elif white > black:
                                                winner = 2
                                            else:
                                                winner = "draw"

                                            a = game.end_screen(screen, winner)
                                            running = False

                        if a == "quit":
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            running1 = False

                        if a == "playagain":
                            pygame.mixer.music.stop()
                            music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                            if os.path.exists(music_path):
                                pygame.mixer.music.load(music_path)
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            running1 = True

                        game.drawgrid(screen)
                        game.drawmarks(screen)
                        pygame.display.update()

                elif buttons["flappy_bird"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("games/flappy_bird.py")

        for name, rect in buttons.items():
            if rect.collidepoint(mouse_pos):
                hovered = name
                break

        screen.blit(background, (0, 0))

        for name, rect in buttons.items():
            if name == hovered:
                draw_glow(screen, rect, glow_colors[name])

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if hovered else pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()