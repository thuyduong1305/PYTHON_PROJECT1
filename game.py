# 1 - Import library
import pygame
from pygame.locals import *
import math
import random

# 2 - Initialize the game (khởi chạy và hiển thị)
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100] #vị trí người chơi
acc=[0,0]  
arrows=[]
arrow = pygame.image.load("resources/images/bullet.png")
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

# 4 - keep looping through

while 1:
    badtimer-=1
# 5 - clear the screen before drawing it again -
    screen.fill(0)
# 6 - draw the screen elements
    for x in range (int(width/grass.get_width()+1)): 
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100)) # vẽ các grass
    screen.blit(castle,(0,30)) # vị trí các thành trì
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))    
    #screen.blit(player, (100,100))
    #screen.blit(player, playerpos)
# 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos() # lấy vị trí của chuột
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    #tính góc hợp giữa hướng của chuột với con thỏ
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    #chuyển góc về radian
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    #
    screen.blit(playerrot, playerpos1)
# 6.2 - Draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*15 # 15 là vận tốc của đạn
        vely=math.sin(bullet[0])*15
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
# 6.3 - Draw badgers
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.3 - Next bad guy
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy) 
    
# 7 - update the screen
    pygame.display.flip()
# 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_SPACE:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEEF:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                keys[0]=False
            elif event.key==pygame.K_DOWN:
                keys[1]=False
            elif event.key==pygame.K_LEFT:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
            # nếu có click chuột, arrows lưu lại góc của position chuột, tức là đạn
# 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5

    #giới hạn thỏ trong khung hình
    
    
