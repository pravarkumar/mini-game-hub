import pygame
import numpy as np
import sys

WIDTH = 825
HEIGHT = 825
min = [0,0,0,0,0,0,0]

class Connect4:
    def __init__(self):
        self.bgcolor = (255, 237, 41)
        self.linecolor = (0, 0, 0)
        self.width = WIDTH
        self.height = HEIGHT
        self.cellsize = self.width // 7

        self.board = np.zeros((7, 7), dtype=int)

        self.current_player = 1
        self.player1 = 1
        self.player2 = 2

    def switch(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def drawgrid(self, screen):
        screen.fill(self.bgcolor)
        for i in range(1, 7):
            pygame.draw.line(screen, self.linecolor, (self.cellsize*i, 0), (self.cellsize*i, self.height), 2)
            pygame.draw.line(screen, self.linecolor, (0, self.cellsize*i), (self.width, self.cellsize*i), 2)

    def drawmarks(self, screen):
        for row in range(7):
            for col in range(7):
                x = col * self.cellsize
                y = (6 - row) * self.cellsize
                center = (x + self.cellsize//2, y + self.cellsize//2)

                outer_radius = self.cellsize // 2 - 5

                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, (255,0,0), center, outer_radius)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(screen, (0,0,255), center, outer_radius)

    def makemove(self, row, col):
        if col < 0 or col >= 7:
            return False
        if min[col] >= 7:
            return False

        self.board[min[col]][col] = self.current_player
        min[col] += 1
        return True

    def checkwin(self):
        b = self.board
        for r in range(7):
            for c in range(7):
                if b[r][c] == 0:
                    continue
                p = b[r][c]
                if c + 3 < 7 and all(b[r][c+i] == p for i in range(4)):
                    return True
                if r + 3 < 7 and all(b[r+i][c] == p for i in range(4)):
                    return True
                if r + 3 < 7 and c + 3 < 7 and all(b[r+i][c+i] == p for i in range(4)):
                    return True
                if r + 3 < 7 and c - 3 >= 0 and all(b[r+i][c-i] == p for i in range(4)):
                    return True
        return False

    def isdraw(self):
        return np.all(self.board != 0)

    def end_screen(self, screen, winner):
        screen.fill((50,50,50))
        font = pygame.font.SysFont(None, 50)

        if winner != "draw":
            text = font.render(f"Player {winner} wins!", True, (255,255,255))
        else:
            text = font.render("Draw!", True, (255,255,255))

        screen.blit(text, (150,150))

        playrect = pygame.Rect(100,300,180,60)
        menurect = pygame.Rect(320,300,180,60)

        pygame.draw.rect(screen,(0,200,0),playrect)
        pygame.draw.rect(screen,(200,0,0),menurect)

        screen.blit(font.render("Play Again", True,(255,255,255)), (110,310))
        screen.blit(font.render("Quit", True,(255,255,255)), (330,310))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if playrect.collidepoint(pos):
                        return "playagain"
                    elif menurect.collidepoint(pos):
                        return "quit"