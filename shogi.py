import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((450,650))
pygame.display.set_caption("Let's Shogi")
font = pygame.font.Font("System.fon",55)
framerate = 30
clock = pygame.time.Clock()

board = [[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None] \
        ,[None,None,None,None,None,None,None,None,None]]
"""
end = True
while end:
    game.input()
    end = game.update()
    draw(game.board)
"""

#駒クラス
class Koma:
    def __init__(self,name,first):
        self.name = name
        self.first = first
#駒インスタンス
ou = Koma("王",True)
gyoku = Koma("玉",True)
hi = Koma("飛",True)
kaku = Koma("角",True)
kin = Koma("金",True)
gin = Koma("銀",True)
kei = Koma("桂",True)
kyo = Koma("香",True)
hu = Koma("歩",True)
ou2 = Koma("王",False)
gyoku2 = Koma("玉",False)
hi2 = Koma("飛",False)
kaku2 = Koma("角",False)
kin2 = Koma("金",False)
gin2 = Koma("銀",False)
kei2 = Koma("桂",False)
kyo2 = Koma("香",False)
hu2 = Koma("歩",False)

#test
board[0][0] = kyo2
board[0][1] = kei2
board[0][2] = gin2
board[0][3] = kin2
board[0][4] = ou2
board[0][5] = kin2
board[0][6] = gin2
board[0][7] = kei2
board[0][8] = kyo2
board[1][1] = hi2
board[1][7] = kaku2
for i in range(9):
    board[2][i] = hu2
for i in range(9):
    board[6][i] = hu
board[8][0] = kyo
board[8][1] = kei
board[8][2] = gin
board[8][3] = kin
board[8][4] = ou
board[8][5] = kin
board[8][6] = gin
board[8][7] = kei
board[8][8] = kyo
board[7][7] = hi
board[7][1] = kaku

class Player:
    def __init__(self,hi_n,kaku_n,kin_n,gin_n,kei_n,kyo_n,hu_n,order):
        self.hi_n = hi_n
        self.kaku_n = kaku_n
        self.kin_n = kin_n
        self.gin_n = gin_n
        self.kei_n = kei_n
        self.kyo_n = kyo_n
        self.hu_n = hu_n
        self.order = order

player1 = Player(0,0,0,0,0,0,0,True)
player2 = Player(0,0,0,0,0,0,0,False)

#背景を描画
def background():
    screen.fill((250,199,66))
    for i in range(8):
        pygame.draw.line(screen,(0,0,0),(50*(i+1),0),(50*(i+1),550))
        pygame.draw.line(screen,(0,0,0),(0,50*(i+3)),(450,50*(i+3)))
    pygame.draw.rect(screen,(0,0,0),(0,0,450,100))
    pygame.draw.rect(screen,(0,0,0),(0,550,450,100))
    
#駒の画像を置く
def set_koma():
    for i in range(9):
        for j in range(9):
            if board[i][j] != None:
                png_name = board[i][j].name + ".png"
                image = pygame.image.load(png_name)
                image = pygame.transform.scale(image,(48,50))
                if board[i][j].first == False:
                    image = pygame.transform.rotate(image,180)
                    screen.blit(image,(50*j+2,50*(i+2)+1))
                else:
                    screen.blit(image,(50*j,50*(i+2)))

#所持駒を表示
def count():
    png_name = ["飛.png","角.png","金.png","銀.png","桂.png","香.png","歩.png"]
    for i in range(7):
        image = pygame.image.load(png_name[i])
        image = pygame.transform.scale(image,(48,50))
        screen.blit(image,(50*i+100,550))
        image = pygame.transform.rotate(image,180)
        screen.blit(image,(300-50*i+2,1))
    char = font.render(str(player1.hi_n),True,(255,255,255))
    screen.blit(char,(120,605))
    char = font.render(str(player1.kaku_n),True,(255,255,255))
    screen.blit(char,(170,605))
    char = font.render(str(player1.kin_n),True,(255,255,255))
    screen.blit(char,(220,605))
    char = font.render(str(player1.gin_n),True,(255,255,255))
    screen.blit(char,(270,605))
    char = font.render(str(player1.kei_n),True,(255,255,255))
    screen.blit(char,(320,605))
    char = font.render(str(player1.kyo_n),True,(255,255,255))
    screen.blit(char,(370,605))
    char = font.render(str(player1.hu_n),True,(255,255,255))
    screen.blit(char,(420,605))
    char = font.render(str(player2.hi_n),True,(255,255,255))
    screen.blit(char,(320,50))
    char = font.render(str(player2.kaku_n),True,(255,255,255))
    screen.blit(char,(270,50))
    char = font.render(str(player2.kin_n),True,(255,255,255))
    screen.blit(char,(220,50))
    char = font.render(str(player2.gin_n),True,(255,255,255))
    screen.blit(char,(170,50))
    char = font.render(str(player2.kei_n),True,(255,255,255))
    screen.blit(char,(120,50))
    char = font.render(str(player2.kyo_n),True,(255,255,255))
    screen.blit(char,(70,50))
    char = font.render(str(player2.hu_n),True,(255,255,255))
    screen.blit(char,(20,50))

def pop(x,y):
    if (y>99 and y<550) or (y<100 and x<350) or (y>549 and x>99):
        x_rect = x-x%50
        y_rect = y-y%50
        if y_rect == 50:
            y_rect = 0
        if y_rect >= 550:
            y_rect = 550
        pygame.draw.rect(screen,(255,0,0),(x_rect,y_rect,51,51),1)
        if y>99 and y<550:
            hold = board[int(x/50)][int(y/50)-2]
"""
def put(x,y):
    if y>99 and y<550:
        board[int(x/50)][int(y/50)-2] = hold
    select = False
"""

class GUI:
    def __init__(self):
        self.x = 350
        self.y = 0
        self.x_board = None
        self.y_board = None

    def reset_hold(self):
        self.x_board = None
        self.y_board = None

    def main(self):
        c = 0
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    self.x,self.y = event.pos
                if event.type == QUIT:
                    event.quit()
                    sys.exit
            background()
            set_koma()
            count()
            pop(self.x,self.y)
            if (self.y<100 and self.x<350):
                self.x_board = 9
                self.y_board = int(self.x/50)
            if (self.y>549 and self.x>99):
                self.x_board = 10
                self.y_board = int(self.x/50)-2
            if self.y>99 and self.y<550:
                self.x_board = int(self.x/50)
                self.y_board = int(self.y/50)-2
            print(self.x_board, self.y_board)
            clock.tick(framerate)
            pygame.display.update()

gui = GUI()
gui.main()