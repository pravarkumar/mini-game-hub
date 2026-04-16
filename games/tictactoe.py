import pygame
import numpy as np
import sys

class TicTacToe:
    def __init__(self,player1,player2):
        self.bgcolor =(28, 170, 156)
        self.ROWS=10
        self.COLS=10
        self.linecolor =(0, 0, 0)
        self.xcolor =(66, 66, 66)
        self.ocolor =(255, 255, 255)
        self.cellsize =82  # each cell is now 240x240
        self.width =self.cellsize*self.ROWS    # board width
        self.height =self.cellsize*self.COLS     # board height
        self.board = np.zeros((self.ROWS,self.COLS))
        self.current_player =player1
        self.player1 =player1
        self.player2 =player2

    def switch(self):
        self.current_player = self.player2 if self.current_player==self.player1 else self.player1

    def drawgrid(self, screen):
        screen.fill(self.bgcolor)
        for i in range(1,self.COLS):
            pygame.draw.line(screen,self.linecolor,(self.cellsize*i,0),(self.cellsize*i,self.height),2)
        for i in range(1,self.ROWS):
            pygame.draw.line(screen,self.linecolor,(0,i*self.cellsize),(self.width,i*self.cellsize),2)

    def drawmarks(self, screen):
        for row in range(10):
            for col in range(10):
                x = col*self.cellsize
                y = row*self.cellsize
                if self.board[row][col]==1:
                    pygame.draw.line(screen, self.xcolor, (x+20,y+20),(x+self.cellsize-20,y+self.cellsize-20),5)
                    pygame.draw.line(screen, self.xcolor, (x+self.cellsize-20,y+20),(x+20,y+self.cellsize-20),5)
                elif self.board[row][col]==2:
                    pygame.draw.circle(screen, self.ocolor, (x+self.cellsize//2, y+self.cellsize//2), self.cellsize//3,5)

    def makemove(self,row,col):
        if self.board[row][col]==0:
            if self.current_player==self.player1:
                self.board[row][col]=1
            else:
                self.board[row][col]=2
            return True
        return False

    def checkwin(self,player):
        if player==self.player1:
            b=(self.board==1)  #convert to True/False grid
        else:
            b=(self.board==2)

        #Horizontal
        h=b[:,:-4] & b[:,1:-3] & b[:,2:-2] & b[:,3:-1] & b[:,4:]

        #Vertical 
        v=b[:-4,:] & b[1:-3,:] & b[2:-2,:] & b[3:-1,:] & b[4:,:]

        #Diagonal 
        d1=b[:-4,:-4] & b[1:-3,1:-3] & b[2:-2,2:-2] & b[3:-1,3:-1] & b[4:,4:]

        #Diagonal 
        d2=b[:-4,4:] & b[1:-3,3:-1] & b[2:-2,2:-2] & b[3:-1,1:-3] & b[4:,:-4]

        return np.any(h) or np.any(v) or np.any(d1) or np.any(d2)

    def isdraw(self):
        return np.all(self.board!=0)

    def end_screen(self, screen, winner):
        # Simple end screen with Play Again and Menu
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