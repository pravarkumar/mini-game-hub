import pygame
import numpy as np
import sys

class TicTacToe:
    def __init__(self):
        self.bgcolor =(28, 170, 156)
        self.linecolor =(23, 145, 135)
        self.xcolor =(66, 66, 66)
        self.ocolor =(239, 231, 200)
        self.cellsize =266  # each cell is now 240x240
        self.width =798    # board width
        self.height =798     # board height
        self.board = np.zeros((3,3))
        self.current_player =1
        self.player1 =1
        self.player2 =2

    

    def switch(self):
        self.current_player = self.player2 if self.current_player==self.player1 else self.player1

    def drawgrid(self, screen):
        screen.fill(self.bgcolor)
        pygame.draw.line(screen, self.linecolor, (self.cellsize,0),(self.cellsize,self.height),5)
        pygame.draw.line(screen, self.linecolor, (2*self.cellsize,0),(2*self.cellsize,self.height),5)
        # Horizontal
        pygame.draw.line(screen, self.linecolor, (0,self.cellsize),(self.width,self.cellsize),5)
        pygame.draw.line(screen, self.linecolor, (0,2*self.cellsize),(self.width,2*self.cellsize),5)

    def drawmarks(self, screen):
        for row in range(3):
            for col in range(3):
                x = col*self.cellsize
                y = row*self.cellsize
                if self.board[row][col]==1:
                    pygame.draw.line(screen, self.xcolor, (x+20,y+20),(x+self.cellsize-20,y+self.cellsize-20),5)
                    pygame.draw.line(screen, self.xcolor, (x+self.cellsize-20,y+20),(x+20,y+self.cellsize-20),5)
                elif self.board[row][col]==2:
                    pygame.draw.circle(screen, self.ocolor, (x+self.cellsize//2, y+self.cellsize//2), self.cellsize//3,5)

    def makemove(self,row,col):
        if self.board[row][col]==0:
            self.board[row][col]=self.current_player
            return True
        return False

    def checkwin(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]!=0:
                return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i]!=0:
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!=0:
            return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]!=0:
            return True
        return False

    def isdraw(self):
        return np.all(self.board!=0)

    def end_screen(self, screen, winner):
        # Simple end screen with Play Again and Menu
        screen.fill((50,50,50))
        font=pygame.font.SysFont(None,50)
        if winner != "draw":
            text = font.render(f"Player {winner} wins!", True, (255,255,255))
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