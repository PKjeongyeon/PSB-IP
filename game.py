import pygame
from warrior import Warrior

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PSB BATTLE GAME")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#define warrior variables
WARRIOR_SIZE = 72
WARRIOR_DATA = [WARRIOR_SIZE]
TANKER_SIZE = 300
TANKER_DATA = [TANKER_SIZE]

#load background img
bg_image = pygame.image.load("img/spacebg.jpg").convert_alpha()


#load spritesheets
warrior_sheet = pygame.image.load("img/warrior.png").convert_alpha()
tanker_sheet = pygame.image.load("img/tanker.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
TANKER_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]



#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#function for drawing warrior health bars
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 3, y - 3, 110, 15))
  pygame.draw.rect(screen, RED, (x, y, 100, 10))
  pygame.draw.rect(screen, YELLOW, (x, y, 100 * ratio, 10))

#create six instances of warrior
warrior_1 = Warrior(50, 50, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
warrior_2 = Warrior(450, 50, TANKER_DATA, tanker_sheet, TANKER_ANIMATION_STEPS )
warrior_3 = Warrior(850, 50)
warrior_4 = Warrior(50, 300)
warrior_5 = Warrior(450, 300)
warrior_6 = Warrior(850, 300)




#game loop
run = True
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(warrior_1.health, 40, 250)
    draw_health_bar(warrior_2.health, 440, 250)
    draw_health_bar(warrior_3.health, 840, 250)
    draw_health_bar(warrior_4.health, 40, 500)
    draw_health_bar(warrior_5.health, 440, 500)
    draw_health_bar(warrior_6.health, 840, 500)

    

    #move worriors
    warrior_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, warrior_2)
    #warrior_2.move()
    #warrior_3.move()

    #draw worriors
    warrior_1.draw(screen)
    warrior_2.draw(screen)
    warrior_3.draw(screen)
    warrior_4.draw(screen)
    warrior_5.draw(screen)
    warrior_6.draw(screen)



    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()



#exit pygame
pygame.quit()