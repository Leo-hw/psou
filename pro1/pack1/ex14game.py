# pygame 모듈을 이용해 게임 프로그램 작성
# anacond prompt창에서 아래 처럼 작성  
# pip install package명 
# import pygame, sys
# from pygame.locals import *
# 
# pygame.init()
# winSurface = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_caption('안녕')
# 
# winSurface.fill((255,255,255))
# 
# pygame.draw.polygon(winSurface, (0,255,0), ((140,0),(290,100),(240,270),(40,270),(0,100)))
# 
# pygame.display.update()
# 
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

import pygame
import math
import random
from pygame import mixer
import time

#mixer.init()
pygame.init()

win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('healthguard')
guard_img=pygame.image.load('resources/mask.png')
fail_img=pygame.image.load('resources/fail.png')
guard_loc=guard_img.get_rect()
destroyer_path=['resources/1.png','resources/2.png','resources/3.png','resources/4.png','resources/5.png']
#sound_effect1 = pygame.mixer.Sound("resources/Popping.wav")
#sound_effect2 = pygame.mixer.Sound("resources/Popping1.wav")

#bak_sound=pygame.mixer.music.load('resources/bk.mp3')
#pygame.mixer.music.play(-1)

direc = 0
destroyer_id=0

class subject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

guard=subject(300,400)
destroyer=[]
fail_count=0
sucess_count=0

def drop():
    des=subject(random.randint(20,950),random.randint(-200,0))    
    randid=random.randint(0,len(destroyer_path)-1)
    speed=(random.randint(1,15))/10     
    destroyer.append([destroyer_id,randid,des,speed])
    print(des.x,des.y)
    

def draw(i):    
    randid=destroyer[i][1]
    print(randid)
    destroyer_img=pygame.image.load(destroyer_path[randid])      
    desx=destroyer[i][2].x
    destroyer[i][2].y+=destroyer[i][3]
    desy=destroyer[i][2].y
    des_loc=destroyer_img.get_rect()
    des_loc.centerx=desx
    des_loc.centery=desy
    guard_loc.centerx=guard.x
    guard_loc.centery=guard.y
    if guard_loc.collidepoint(des_loc.centerx,des_loc.centery)==True: 
        #sound_effect1.play()       
        destroyer.pop(i)
        global sucess_count
        sucess_count+=1            
    elif desy>=600:
        destroyer.pop(i)
        global fail_count
        fail_count+=1        
    else:        
        win.blit(destroyer_img, (desx,desy))
    if len(destroyer)<3:
        drop()
    return sucess_count,fail_count
    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    win.fill((246, 191, 249))
    guide= pygame.font.SysFont('freesansbold.tff', 25).render("press up/down/left/right key to move the mask " ,1,(0, 0, 255))       
    win.blit(guide,(20,20))
    
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_RIGHT] and guard.x < 870:
        guard.x += 3
    if keypress[pygame.K_LEFT] and guard.x > -50:
        guard.x -= 3
    if keypress[pygame.K_UP]:
        guard.y -= 3
    if keypress[pygame.K_DOWN]:
        guard.y += 3
    if fail_count<=20:
        if len(destroyer)<3:
            drop()
        for i in range(len(destroyer)):
            draw(i)
    else:
        win.blit(fail_img,(400,180))

    score = pygame.font.SysFont('freesansbold.tff', 25).render("Score: " + str(sucess_count),1,(0, 255, 0))
    fail= pygame.font.SysFont('freesansbold.tff', 25).render("Fail: " + str(fail_count),1,(255, 0, 0))

    win.blit(score,(800,20))
    win.blit(fail,(800,50))
      
    win.blit(guard_img,(guard.x,guard.y))

    pygame.display.update()

