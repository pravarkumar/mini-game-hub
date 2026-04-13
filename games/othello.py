import pygame
import numpy as np
import sys

WIDTH = 800
HEIGHT = 850

class Othello:
    def __init__(self):
        self.bgcolor = (0, 120, 0)
        self.linecolor = (0, 0, 0)
        self.width = WIDTH
        self.height = WIDTH
        self.cellsize = self.width // 8

        self.board = np.zeros((8, 8), dtype=int)
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2

        self.current_player = 1
        self.player1 = 1
        self.player2 = 2

    def switch(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def drawgrid(self, screen):
        screen.fill(self.bgcolor)
        for i in range(1, 8):
            pygame.draw.line(screen, self.linecolor, (self.cellsize*i, 0), (self.cellsize*i, self.height), 2)
            pygame.draw.line(screen, self.linecolor, (0, self.cellsize*i), (self.width, self.cellsize*i), 2)

    def drawmarks(self, screen):
        for row in range(8):
            for col in range(8):
                x = col * self.cellsize
                y = row * self.cellsize
                center = (x + self.cellsize//2, y + self.cellsize//2)

                outer_radius = self.cellsize // 2 - 5
                inner_radius = outer_radius - 4

                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, (255,255,255), center, outer_radius)
                    pygame.draw.circle(screen, (0,0,0), center, inner_radius)

                elif self.board[row][col] == 2:
                    pygame.draw.circle(screen, (0,0,0), center, outer_radius)
                    pygame.draw.circle(screen, (255,255,255), center, inner_radius)

    # CORRECT MOVE VALIDATION
    def move_isvalid(self, row, col):
        if self.board[row][col] != 0:
            return False

        opponent = self.player2 if self.current_player == self.player1 else self.player1

        directions = [(-1,0),(1,0),(0,-1),(0,1),
                      (-1,-1),(-1,1),(1,-1),(1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False

            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == opponent:
                    found_opponent = True
                elif self.board[r][c] == self.current_player:
                    if found_opponent:
                        return True
                    break
                else:
                    break
                r += dr
                c += dc

        return False

    # CORRECT MAKEMOVE
    def makemove(self, row, col):
        if not self.move_isvalid(row, col):
            return False

        self.board[row][col] = self.current_player
        opponent = self.player2 if self.current_player == self.player1 else self.player1

        directions = [(-1,0),(1,0),(0,-1),(0,1),
                      (-1,-1),(-1,1),(1,-1),(1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []

            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == opponent:
                    to_flip.append((r, c))
                elif self.board[r][c] == self.current_player:
                    for rr, cc in to_flip:
                        self.board[rr][cc] = self.current_player
                    break
                else:
                    break
                r += dr
                c += dc

        return True

    #  CHECK IF PLAYER HAS ANY VALID MOVE
    def valid_possible(self, player):
        current = self.current_player
        self.current_player = player

        for r in range(8):
            for c in range(8):
                if self.move_isvalid(r, c):
                    self.current_player = current
                    return True

        self.current_player = current
        return False

    # GAME OVER CHECK
    def checkwin(self):
        black = np.sum(self.board == 1)
        white = np.sum(self.board == 2)

        if black + white == 64:
            return True

        if not self.valid_possible(self.player1) and not self.valid_possible(self.player2):
            return True

        return False

    # DRAW CHECK
    def isdraw(self):
        black = np.sum(self.board == 1)
        white = np.sum(self.board == 2)
        return black == white

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