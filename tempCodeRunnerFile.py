import pygame
import sys
import os
import subprocess
import numpy as np
from games.tictactoe import TicTacToe

WIDTH = 800
HEIGHT = 850

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
    "flappy_bird": pygame.Rect(83, 260, 634, 117),
    "othello": pygame.Rect(85, 386, 634, 117),
    "connect4": pygame.Rect(84, 512, 634, 117),
    "tictactoe": pygame.Rect(85, 632, 634, 118),
    "exit": pygame.Rect(83, 765, 634, 117),
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
    running1=True
    while running1:
        mouse_pos = pygame.mouse.get_pos()
        hovered = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["exit"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                elif buttons["tictactoe"].collidepoint(pos):
                    game=TicTacToe()
                    pygame.display.set_caption("Tic Tac Toe")

                    running=True

                    while running:
                        a="idk"
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

                            running1=False
                        if a== "playagain":
                            #code for leaderboard.sh
                            running1=True

                        game.drawgrid(screen)
                        game.drawmarks(screen)
                        pygame.display.update()

                elif buttons["connect4"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("games/connect4.py")

                elif buttons["othello"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("games/othello.py")

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