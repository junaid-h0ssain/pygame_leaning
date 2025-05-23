# Example file showing a circle moving on screen
import pygame
import random
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
speed = 1000
bug_speed = 500
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.5)
bug_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 3.5)
playerImg = pygame.image.load('assets/rocket.png')
bugImg = pygame.image.load('assets/bug.png')
# player_x_pos = 400
# player_y_pos = 400
bug_movex = bug_pos.x
bug_movey = bug_pos.y
i = 0
def player(xpos,ypos):
    screen.blit(playerImg,(xpos,ypos) )

def bug(xpos,ypos,ranmin):
    screen.blit(bugImg,(xpos,ypos) )
    global bug_movex
    global bug_movey
    if bug_pos.x !=bug_movex:# and bug_pos.y != bug_movey:
        if bug_pos.x <bug_movex and bug_pos.x<1280:
            bug_pos.x += bug_speed * dt
        if bug_pos.x >bug_movex and bug_pos.x>0:
            bug_pos.x -= bug_speed * dt
    if bug_pos.x ==bug_movex:
        bug_movex = random.randint(0,1280)-ranmin
        bug_movey = random.randint(0,720)+ranmin
        print(bug_movex,bug_movey)
        bug_movex-=1
        
        if bug_pos.y >bug_movey:
            bug_pos.y -= bug_speed * dt
        else:
            bug_pos.y += bug_speed * dt

    if bug_movex<=0 or bug_movey<=0:
        bug_movex = random.randint(0,1280)-ranmin
        bug_movey = random.randint(0,720)+ranmin
        print(bug_movex,bug_movey)
    else:
        bug_movex-=1
        bug_movey-=1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player(player_pos.x,player_pos.y)
    bug(bug_pos.x+150,bug_pos.y-50,500)
    bug(bug_pos.x,bug_pos.y,100)
    bug(bug_pos.x-100,bug_pos.y+100,150)
    #bug(xpos_bug,ypos_bug)
    #bug_movement()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y >0:
            player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        if player_pos.y <650:
            player_pos.y += speed * dt
    if keys[pygame.K_a]:
        if player_pos.x >0:
            player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        if player_pos.x <1220:
            player_pos.x += speed * dt 
   
    # if bug_pos.y >bug_movey:
    #     bug_pos.y -= bug_speed * dt
    # if bug_pos.x >=bug_movex:
    #     bug_pos.x -= bug_speed * dt
    # if bug_pos.y <bug_movey:
    #     bug_pos.y += bug_speed * dt
    # if bug_pos.x <bug_movex:
    #     bug_pos.x += bug_speed * dt

   

    if ((bug_movex>=(player_pos.x-140)) and (bug_movex <=(player_pos.x+140))) and ((bug_movey>=(player_pos.y-140)) and (bug_movey <=(player_pos.y+140))):
        #print(f'Hit!!{i}')
        i+=1
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()