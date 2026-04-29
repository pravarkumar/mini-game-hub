import pygame
import sys
import csv
import os
import subprocess
import numpy as np
from games.tictactoe import TicTacToe
from games.othello import Othello
from games.connect4 import Connect4
from games.base import Game
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import collections

WIDTH = 825
HEIGHT = 825

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game Hub")

clock = pygame.time.Clock()

# Base directory

# Background
image_path = os.path.join(BASE_DIR, "images/Menu_final.png")
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player1=sys.argv[1]
player2=sys.argv[2]

a="playagain"

# Music
music_path = "sound_effects/menu_music.mp3"
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
    "othello": pygame.Rect(74, 288, 678, 126),
    "connect4": pygame.Rect(74, 420, 678, 128),
    "tictactoe": pygame.Rect(74, 560, 678, 126),
    "exit": pygame.Rect(76, 692, 678, 117),
}

glow_colors = {
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

def recordres(winner, loser, game_name, draw=False):
    history_path="history.csv"
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
    subprocess.run([r"bash",lpath,sortby])

def show_charts():
    history_path = "history.csv"
    if not os.path.exists(history_path):
        return

    winners = []
    games_played = []

    with open(history_path, newline="") as f:
        for row in csv.reader(f):
            if len(row) < 4:
                continue

            if row[3] == "win" and row[0] != "draw":
                winners.append(row[0])

            games_played.append(row[2])

    fig, (ax1, ax2)=plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("#1a1a2e")

    #BAR CHART
    win_counts = collections.Counter(winners).most_common(5)

    
    names=[]
    counts=[]

    for name, count in win_counts:
        names.append(name)
        counts.append(count)

    ax1.bar(names,counts,
            color=["#e94560", "#0f3460", "#533483", "#f5a623", "#16213e"],
            edgecolor="white" )

    ax1.set_facecolor("#16213e")
    ax1.set_title("Top 5 Players by Wins", color="white", fontsize=22)

    ax1.tick_params(axis="x", colors="white", labelsize=18)
    ax1.tick_params(axis="y", colors="white", labelsize=18)

    #PIE CHART -
    game_counts = collections.Counter(games_played)

    
    ax2.pie(
            game_counts.values(),
            labels=game_counts.keys(),
            autopct="%1.1f%%",
            colors=["#e94560", "#0f3460", "#533483", "#f5a623"],
            textprops={"color": "white", "fontsize": 18}
        )

    ax2.set_title("Most Played Games", color="white", fontsize=22)
    plot_path="images/plot.png"
    plt.savefig(plot_path)
    plt.close()

    chart_surf = pygame.image.load(plot_path)

    cw, ch = chart_surf.get_size()
    sw, sh = screen.get_size()

    scale = min(sw / cw, sh / ch)
    new_w, new_h = int(cw * scale), int(ch * scale)

    chart_surf = pygame.transform.scale(chart_surf, (new_w, new_h))

    x = (sw - new_w) // 2
    y = (sh - new_h) // 2

    screen.fill((26, 26, 46))
    screen.blit(chart_surf, (x, y))

    font = pygame.font.SysFont(None, 32)
    msg = font.render("Press any key to continue", True, (255, 255, 255))

    screen.blit(msg,(screen.get_width() // 2 - msg.get_width() // 2,screen.get_height() - 100))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return
    
def runothello():
    global a
    global screen
    pygame.mixer.music.stop()
    music_path = "sound_effects/Othello.mp3"
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
    show_charts()
    a=game.end_screen(screen,winner)

    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Mini Game Hub")
    pygame.mixer.music.stop()
    music_path = "sound_effects/menu_music.mp3"
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    else:
        print("menu_music.mp3 not found!")




def runtictactoe():
    global a
    global screen
    game=TicTacToe(player1,player2)#We call the constructor of the class TicTacToe like c=int() is also valid it means that c will be of class int and have the initial value = 0 like c=1 is same as c=int(1)
    screen=pygame.display.set_mode((game.width,game.height))
    pygame.display.set_caption("Just a quiet game of Tic Tac Toe ⭕❌🎮")# This text will come at the top of the screen of the game 
    pygame.mixer.music.stop()
    music_path ="sound_effects/TicTacToe.mp3"
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
    show_charts()
    a=game.end_screen(screen,winner)

    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Mini Game Hub")
    pygame.mixer.music.stop()
    music_path = "sound_effects/menu_music.mp3"
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    else:
        print("menu_music.mp3 not found!")



def runconnect4():
    global a
    global screen
    pygame.mixer.music.stop()
    music_path="sound_effects/Connect4.mp3"
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
    show_charts()
    a=game.end_screen(screen,winner)

    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Mini Game Hub")
    pygame.mixer.music.stop()
    music_path = "sound_effects/menu_music.mp3"
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    else:
        print("menu_music.mp3 not found!")






def main():
    global screen
    global a
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
                    runtictactoe()

                elif buttons["connect4"].collidepoint(pos):
                    runconnect4()

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