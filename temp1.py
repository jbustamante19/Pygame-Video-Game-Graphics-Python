# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame, sys
from pygame.locals import *
import math
from pylab import *



#physical calculations and constants
'''    
degreestheta= 60

theta = (degreestheta*(pi/180)) 
degreesphi=20
phi= (degreesphi*(pi/180))  

g = -10
v0= 50


trange =(-2*(v0*sin(phi))/g)
t = linspace(0,trange,30)


vx0 = v0*cos(theta)
vy0 = v0*sin(theta)
vz0 = v0*sin(phi)



x = (vx0*t )
y = (vy0*t ) 
z = 15*(vz0 * t + (0.5 * g * (t**2)))

#array with height and width of the ball along trajectory

width= linspace(32,20,30)

height =linspace(32,20,30)
'''
       
#initialization of pygame(requiered)
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#setup of window
screen = pygame.display.set_mode((626, 626))
pygame.display.set_caption('Penalty Kicks!')

#uploading of multiple picture and defining initial positions 
import os

folder = os.path.dirname(os.path.realpath(__file__))

gloves2 = pygame.image.load(os.path.join(folder, "gloves2.png"))
#gloves2 = pygame.image.load('gloves2.png')
gloves = pygame.transform.scale(gloves2,(64,64))

glovesx= 275
glovesy=270

professor2 = pygame.image.load(os.path.join(folder, "roman4.jpg"))
#professor2 = pygame.image.load('roman4.jpg')

professor=pygame.transform.scale(professor2,(35,50)) 

profx=290
profy=260

suck = pygame.image.load(os.path.join(folder, "suck.png"))
#suck = pygame.image.load('suck.png')
suckx=320
sucky=280

score = pygame.image.load(os.path.join(folder, "goal.png"))
#score = pygame.image.load('goal.png')
scorex = 160
scorey= 10

xinit = 330#ball
yinit=500#ball


arrow2 = pygame.image.load(os.path.join(folder, "arrow.png"))
#arrow2 = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow2,(55,55))

line2 = pygame.image.load(os.path.join(folder, "velocity.png"))
#line2 =pygame.image.load('velocity.png') 
linex = 500
liney=450

ball = pygame.image.load(os.path.join(folder, "ball4.png"))
#ball = pygame.image.load('ball4.png')

background = pygame.image.load(os.path.join(folder, "field3.jpg"))
#background = pygame.image.load('field3.jpg')


l =.1 # iterator between .1 can serve as game speed adjuster
goalie=False

#defining of some variables
c=1
xchange=0
ychange=0

xfinal = 0
result=''
intro = True
game=False
thetachange=0
vchange=0
phichange=0
degreestheta= 80
degreesphi=20
v0= 40
g = -10




#array with height and width of the ball along trajectory
width= linspace(32,20,30)

height =linspace(32,20,30)

#myfont = pygame.font.SysFont("monospace", 30)
while intro:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    thetachange+=1
                
                if event.key == pygame.K_RIGHT:
                    thetachange-=1
                if event.key == pygame.K_DOWN:
                    vchange-=1
                if event.key == pygame.K_UP:
                    vchange+=1
             
                if event.key == pygame.K_SPACE:
                    phichange+=.5
                    
                if event.key == pygame.K_RETURN:
                    game = True
                    intro = False
                if event.key == pygame.K_g:
                    goalie=False
                    
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    thetachange=0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    vchange=0
            if event.key == pygame.K_SPACE:
                    phichange=0
    #label = myfont.render("Some text!", 1, (10,10,10))
    degreestheta+=thetachange
    theta = (degreestheta*(pi/180))
    degreesphi+=phichange
    phi= (degreesphi*(pi/180))
    
    v0+=vchange
    
    arrow2 = pygame.transform.rotate(arrow,degreestheta)
    
    line = pygame.transform.smoothscale(line2,(50,v0))
    screen.blit(line,(linex,liney))
    screen.blit(arrow2,(xinit-15,yinit-30))
    screen.blit(ball,(xinit,yinit))
    screen.blit(professor,(profx,profy))
    screen.blit(gloves,(glovesx,glovesy))
    #screen.blit(label, (100, 100))
    
    
    
    
    
    
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
#physical calculations
    
        
trange =(-2*(v0*sin(phi))/g)
t = linspace(0,trange,30)


vx0 = v0*cos(theta)
vy0 = v0*sin(theta)
vz0 = v0*sin(phi)



x = (vx0*t )
y = (vy0*t ) 
z = 15*(vz0 * t + (0.5 * g * (t**2)))    
    
    
 

    
    

#this is my main loop or so called 'Game-Loop'
while game: 
    
    #displays background
    screen.blit(background, (0,0))
    
    #controls events aka user interaction with program
    
    for event in pygame.event.get():
        
        #defines x and y change if goal-keeper mode is on        
        if goalie==True:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    xchange=3
                if event.key == pygame.K_LEFT:
                    xchange=-3
                if event.key == pygame.K_DOWN:
                    ychange=3
                if event.key == pygame.K_UP:
                    ychange=-3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    xchange=0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    ychange=0
        #provides player with option of quiting      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #keeps track of glove position change  
    glovesx+=xchange
    glovesy+=ychange
    
    #method that is called to determine if the Goal-keeper blocks the ball
    def block(glovesx,glovesy,zpos):
        if  (x[29]+xinit>glovesx and x[29]+xinit<glovesx +70) and (zpos>glovesy and zpos<glovesy+30):
            return True
    
   
   
   

   #ball controlls
    if c<=15 :
        #ball2 = pygame.transform.smoothscale(ball, (int(width[c]), int(height[c])))
        screen.blit(ball,(x[int(c)]+xinit, yinit-z[int(c)])) 
        c+=l
        
        
    if c>15 and z[int(c)]>=y[29]:
        #ball2 = pygame.transform.smoothscale(ball, (int(width[c]), int(height[c])))
        screen.blit(ball,(x[int(c)]+xinit, yinit-z[int(c)])) 
        xfinal=x[int(c)]
        c+=l
        
    # establishes conditions for not scoring
    if  (c>15 and yinit-z[int(c)]>360) or ( yinit-z[int(c)]<=360 and yinit-z[int(c)]<=223) or ( (x[29]+xinit<193 or x[29]+xinit>428)) or block(glovesx,glovesy,yinit-z[int(c)]):
         
        result = 'miss'
    
    
    
    
    #Automated goalie if goal-keeper mode is off    
    if goalie==False:
        if profx<xfinal+xinit :
            xchange=1
            if profx==xfinal+xinit:
                xchange=0
            
        if profx>xfinal+xinit :
            xchange=-1
            
            if profx==xfinal+xinit:
                xchange=0
         
            
       
    profx+=xchange
    profy+=ychange    
        
    suckx+=xchange
    sucky+=ychange
    
    if result=='miss':
        screen.blit(suck,(suckx, sucky))   
    if c>15 and result=='':
        screen.blit(ball,(x[int(c)]+xinit, yinit-z[int(c)]))
        screen.blit(score,(scorex,scorey))
        
            
           
            
    screen.blit(professor,(profx,profy))
    screen.blit(gloves,(glovesx,glovesy))
    
    pygame.display.update()
    fpsClock.tick(FPS)



'''
https://pythonprogramming.net/pygame-python-3-part-1-intro/
http://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate
https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q=arrow&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=ift:png#newwindow=1&safe=off&hl=en&tbs=ift:png&tbm=isch&q=arrow&imgrc=_H6Scp-W4BsQgM%3A

'''





