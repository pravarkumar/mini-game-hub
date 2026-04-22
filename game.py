import pygame
import sys
import csv
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

player1=sys.argv[1]
player2=sys.argv[2]

# Music
music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
else:
    print("menu_music.mp3 not found!")



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

def recordres(winner, loser, game_name, draw=False):
    history_path = os.path.join(BASE_DIR, "history.csv")
    with open(history_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            winner,
            loser,
            game_name,
            "draw" if draw else "win",
        ])

def askpref(game):
    darkscr=pygame.Surface((game.width, game.height), pygame.SRCALPHA)
    darkscr.fill((0,0,0,180))
    screen.blit(darkscr,(0,0))
    font=pygame.font.SysFont(None,38)

    title=font.render("Sort leaderboard by:",True,(255, 255, 255))
    screen.blit(title, (game.width//2-title.get_width()//2,250))

    wins= pygame.Rect(100, 340, 170, 55)
    losses= pygame.Rect(315, 340, 170, 55)
    ratio= pygame.Rect(530, 340, 170, 55)

    for rect,name,col in [
        (wins,"Wins",(0, 180, 80)),(losses, "Losses",(200, 80, 0)),(ratio,"Ratio",(0, 100, 220)),
    ]:
        pygame.draw.rect(screen,col,rect)
        txt=font.render(name,True,(255, 255, 255))
        screen.blit(txt,(rect.centerx - txt.get_width()//2, rect.centery - txt.get_height()//2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wins.collidepoint(event.pos):
                    return "wins"
                if losses.collidepoint(event.pos):
                    return "losses"
                if ratio.collidepoint(event.pos):
                    return "ratio"

def leaderboard(sortby):
    lpath=os.path.join(BASE_DIR, "leaderboard.sh")
    subprocess.run(["bash",lpath,sortby])



def main():
    global screen
    running1=True #tells the status of this running process 
    while running1:# if true then runs 
        a="playagain"# name anything like will not chnage if no clicks of quit or play_again
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
                    game=TicTacToe(player1,player2)#We call the constructor of the class TicTacToe like c=int() is also valid it means that c will be of class int and have the initial value = 0 like c=1 is same as c=int(1)
                    screen=pygame.display.set_mode((game.width,game.height))
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
                         
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type==pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                row = y//game.cellsize
                                col = x//game.cellsize

                                
                                if game.makemove(row, col):
                                    if game.checkwin(game.current_player):
                                        winner = game.current_player  # current player just won
                                        loser = game.player1 if game.current_player==game.player2 else game.player2
                                        recordres(winner,loser,"tictactoe")
                                        running = False
                                    elif game.isdraw():
                                        winner="draw"
                                        recordres(game.player1,game.player2,"tictactoe",draw=True)
                                        running = False
                                    else:
                                        game.switch()
                        if running:
                            game.drawgrid(screen)
                            game.drawmarks(screen)
                            pygame.display.update()#Easy code :)
                    game.drawmarks(screen)
                    sortby=askpref(game)
                    leaderboard(sortby)
                    a=game.end_screen(screen,winner)

                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    pygame.display.set_caption("Mini Game Hub")
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("menu_music.mp3 not found!")

                        

                elif buttons["connect4"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "Connect4.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("Connect4.mp3 not found!")

                    game = Connect4(player1,player2)
                    pygame.display.set_caption("Keeping it simple—connect 4 🔴🔵")
                    running=True

                    while running:
                        
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
                                        loser=game.player1 if game.current_player==game.player2 else game.player2
                                        recordres(winner,loser,"connect4")
                                        running = False
                                    elif game.isdraw():
                                        winner="draw"
                                        recordres(game.player1,game.player2,"connect4",draw=True)
                                        running = False
                                    else:
                                        game.switch() 
                            
                        if running:
                            game.drawgrid(screen)
                            game.drawmarks(screen)
                            pygame.display.update()#Easy code :)
                    game.drawmarks(screen)
                    sortby=askpref(game)
                    leaderboard(sortby)
                    a=game.end_screen(screen,winner)

                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    pygame.display.set_caption("Mini Game Hub")
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("menu_music.mp3 not found!")

                elif buttons["othello"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "Othello.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("Othello.mp3 not found!")

                    game = Othello(player1,player2)
                    pygame.display.set_caption("Othello ⚫⚪ :)")
                    running = True

                    while running:
                        

        #  CHECK GAME END (both players stuck)
                        if (not game.valid_possible(game.player1) and not game.valid_possible(game.player2)):

                            black = np.sum(game.board == 1)
                            white = np.sum(game.board == 2)

                            if black > white:
                                winner = player1
                                loser=player2
                            elif white > black:
                                winner = player2
                                loser=player1
                            else:
                                winner =game.player1
                                loser=game.player2
                            recordres(winner,loser,"othello",draw=True)
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
                                                winner = player1
                                                loser = player2
                                            elif white > black:
                                                winner = player2
                                                loser=player1
                                            else:
                                                winner = "draw"
                                                loser="draw"
                                            recordres(winner,loser,"othello")
                                            running = False
                        if running:
                            game.drawgrid(screen)
                            game.drawmarks(screen)
                            pygame.display.update()#Easy code :)
                    game.drawmarks(screen)
                    sortby=askpref(game)
                    leaderboard(sortby)
                    a=game.end_screen(screen,winner)

                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    pygame.display.set_caption("Mini Game Hub")
                    pygame.mixer.music.stop()
                    music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    else:
                        print("menu_music.mp3 not found!")
                        

                elif buttons["flappy_bird"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("games/flappy_bird.py")
        
        if a=="quit":
            running1=False

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