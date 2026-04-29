import pygame
import numpy as np
import sys

WIDTH = 825
HEIGHT = 825


class Connect4:
    def __init__(self,player1,player2):
        self.bgcolor = (255, 237, 41)
        self.linecolor = (0, 0, 0)
        self.width = WIDTH
        self.height = HEIGHT
        self.cellsize = self.width // 7
        self.mn=[0,0,0,0,0,0,0]
        self.board = np.zeros((7, 7), dtype=int)

        self.current_player=player1
        self.player1=player1
        self.player2=player2

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
        if self.mn[col] >= 7:
            return False

        self.board[self.mn[col]][col] = 1 if self.current_player==self.player1 else 2
        self.mn[col] += 1
        return True

    def checkwin(self):
        b = self.board
        #Horizontal
        if(np.any( ((b[:,0:-3]==b[:,1:-2]) & (b[:,0:-3] == b[:,2:-1]) & (b[:,0:-3]==b[:,3:]) & (b[:,0:-3]!=0)) )):
            return True
        
        #Vertical
        if(np.any(  (b[0:-3,:]==b[1:-2,:]) & (b[0:-3,:]==b[2:-1,:]) & (b[0:-3,:]==b[3:,:]) & (b[0:-3,:]!=0))):
            return True
        #Diagonals
        if(np.any(  (b[:-3,:-3]==b[1:-2,1:-2]) & (b[:-3,:-3] == b[2:-1,2:-1]) & (b[:-3,:-3]==b[3:,3:]) & (b[:-3,:-3]!=0))):
            return True
        
        if(np.any((b[3:,3:]==b[2:-1,2:-1]) & (b[3:,3:]==b[1:-2,1:-2]) & (b[3:,3:]==b[:-3,:-3]) & (b[3:,3:]!=0))):
            return True
        return False

        

    def isdraw(self):
        return np.all(self.board != 0)

    def end_screen(self, screen, winner):
        screen.fill((50,50,50))
        font=pygame.font.SysFont(None,50)
        if winner != "draw":
            text = font.render(f"{winner} Wins!", True, (255,255,255))
        else:
            text = font.render("Draw!", True, (255,255,255))
        screen.blit(text, (150,150))
        # Buttons
        playrect = pygame.Rect(100,300,180,60)
        menurect = pygame.Rect(320,300,180,60)
        pygame.draw.rect(screen,(0,200,0),playrect)
        pygame.draw.rect(screen,(200,0,0),menurect)
        playtext = font.render("Play Again", True,(255,255,255))
        menutext = font.render("Quit", True,(255,255,255))
        screen.blit(playtext,(110,310))
        screen.blit(menutext,(330,310))
        pygame.display.update()
        waiting=True
        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    if playrect.collidepoint(pos):
                        
                        return "playagain"
                    elif menurect.collidepoint(pos):
                        return "quit"