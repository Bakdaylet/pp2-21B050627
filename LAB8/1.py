import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("street.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
    
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
#Creating class coin                  
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.speed = 3
    def move(self):
        
        self.rect.move_ip(0,3)
        if (self.rect.top > 600):
            
            self.rect.top = 0
              
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
            
    def check_collision(self, player):
        if pygame.sprite.collide_rect(self, player):
            return True
        return False
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin() 
#Creating Sprites Groups

coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1) 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
   
 
    #Moves and Re-draws all Sprites
    for coin in coins:
     DISPLAYSURF.blit(coin.image, coin.rect)
    coin.update()
    if coin.check_collision(P1):
        COINSCORE += 1
        SCORE += 1
        coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    coinscores = font_small.render("Coins: " + str(COINSCORE), True, BLACK)
    DISPLAYSURF.blit(coinscores, (293,10))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          DISPLAYSURF.blit(scores, (50, 500))
          DISPLAYSURF.blit(coinscores, (50, 520)) 
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)