#I Wanna Defeat Evil Mike Tyson

#1 -Packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
import random

#2 - Constants
WINDOW_HEIGHT = 960
WINDOW_WIDTH = 1024

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FRAMES_PER_SECOND = 50
N_PIXELS_PER_FRAME = 5

SCORE = 0

KID_X = 640
KID_Y = 880

kidX = KID_X
kidY = KID_Y

KID_HP = 3

N_PIXELS_TO_MOVE = 7
N_PIXELS_UP = 115

PLAYER_GRAVITY = 4
falling = False
nJumps = 0

STATE_START = 'start'
STATE_GAME = 'game'
STATE_RESULTS = 'results'


#3 - Initialize the World
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

#4 - Load Images
playButton = pygwidgets.TextButton(window, (100,750), 'Play Game', width=150, height=75)

messageTextField = pygwidgets.DisplayText(window, (10, 20), '', \
                                    fontSize=36, textColor=WHITE)

messageTextField2 = pygwidgets.DisplayText(window, (10,50), '', \
                                    fontSize=36, textColor=WHITE)

healthText = pygwidgets.DisplayText(window, (175,80), '', \
                                             fontSize=38, textColor=WHITE)

scoreText = pygwidgets.DisplayText(window, (50,80), '', \
                                             fontSize=38, textColor=WHITE)

messageTextField.setValue('Mike Tyson has turned EVIL and is raining spikes upon the world.')
messageTextField2.setValue('Avoid the Spikes and defeat his clones to save the world!')

PUNCH_OUT = pygame.image.load("images/Punchout.png").convert()

scoreText.setValue('Score: ' + str(SCORE))
healthText.setValue('Health: ' + str(KID_HP))

kid = pygwidgets.ImageCollection(window,(KID_X,KID_Y), \
                                 {"right":"images/TheKid/FaceRight.png","left":"images/TheKid/FaceLeft.png"}, "right")
kid.scale(200)

kidRect = pygame.Rect(kidX, kidY, 10, 10)

#5 - Initialize Variables
MAX_HEIGHT = WINDOW_HEIGHT - 10
MAX_WIDTH = WINDOW_WIDTH - 10

spikeX = random.randrange(MAX_WIDTH)
spikeY = random.randrange(MAX_HEIGHT)

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

N_SPIKES = 20
SPIKE_WIDTH = 32
SPIKE_HEIGHT = 32
SPIKE_Y = random.randrange(MAX_HEIGHT)
spikeY = spikeY + ySpeed

#Spikes Lists
sYlist = [ ]
sXlist = [ ]
spikeSpeedList = [ ]
spikeImgList = [ ]
sHList = [ ]
sWList = [ ]

#Falling Spikes Loop *append to lists
for index in range(0 , N_SPIKES):
    spike = pygwidgets.Image(window, (SPIKE_Y, -5), "images/Killers/SpikesDown.png")
    spikeImgList.append(spike)
    spikeSpeedList.append(N_PIXELS_PER_FRAME)
    sXlist.append(random.randrange(MAX_WIDTH))
    sYlist.append(random.randrange(-300, -10))

#Tyson Constants
TYSON_Y = 820
TYSON_X = 1
N_TYSON = 3
TYSON_WIDTH = 30
TYSON_HEIGHT = 108

#Tyson Lists
tYlist = [ ]
tXlist = [ ]
tysonSpeedList = [ ]
tysonImgList = [ ]
tHList = [ ]
tWList = [ ]

#Tyson Attack *append to lists
for index in range(0, N_TYSON):
    tyson = pygwidgets.ImageCollection(window, (TYSON_X, TYSON_Y), \
        {"stance":"images/Killers/MTleft.png", "uppercut":"images/Killers/MTuppercut.png", "death":"images/Killers/MTdeath.png"}, "stance")
    tysonImgList.append(tyson)
    tysonSpeedList.append(N_PIXELS_PER_FRAME)
    tXlist.append(TYSON_X)

#World
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
state = STATE_START

#6 - Game Loop Forever
while True:
    #7 - Event Checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if state == STATE_START:
            if playButton.handleEvent(event):
                state = STATE_GAME
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if nJumps < 2:
                    kidY = kidY - N_PIXELS_UP
                    falling = True
                    kid.setLoc((kidX, KID_Y))
                    nJumps = nJumps + 1

    #8 - PER FRAME Actions
    #Kid Movement
    keyPressedList = pygame.key.get_pressed()
    #Move Left       
    if keyPressedList[pygame.K_LEFT]:
        kid.replace("left") 
        kidX = kidX - N_PIXELS_TO_MOVE
        kid.setLoc((kidX, kidY))
    #Move Right
    if keyPressedList[pygame.K_RIGHT]:
        kid.replace("right")
        kidX = kidX + N_PIXELS_TO_MOVE
        kid.setLoc((kidX, kidY))

    #Gravity
    if falling == True:
        kidY = kidY + PLAYER_GRAVITY
        if kidY >= KID_Y:
            falling = False
            kidY = KID_Y
            nJumps = 0
        kid.setLoc((kidX, kidY))

    #Falling Spikes Loop *execute
    for index in range(0, N_SPIKES):
        sYlist[index] = sYlist[index] + spikeSpeedList[index]
        spikeImgList[index].setLoc((sXlist[index], sYlist[index]))
        if sYlist[index] > WINDOW_HEIGHT:
            sXlist[index] = random.randrange(MAX_WIDTH)
            sYlist[index] = random.randrange(-300, -10)
              
    #Tyson Loop *execute
    for index in range(0, N_TYSON):
        TYSON_X = random.randrange(1,3)
        tXlist[index] = tXlist[index] + tysonSpeedList[index]
        tysonImgList[index].setLoc((tXlist[index], TYSON_Y))
        if tXlist[index] > WINDOW_WIDTH:
            tXlist[index] = random.randrange(-500, -20)

    #Spike Collision
    for index in range (0, N_SPIKES):
        spikeRect = pygame.Rect(sXlist[index], sYlist[index], SPIKE_WIDTH, SPIKE_HEIGHT)
        #if spikeRect.colliderect(kidRect):
            #print('collision')

    #Tyson Collision
    for index in range (0, N_TYSON):
        mykeRect = pygame.Rect(tXlist[index], TYSON_Y, TYSON_WIDTH, TYSON_HEIGHT)
        if mykeRect.colliderect(kidRect):
            print('collision')


    #ScreenBlock(Width)
    if kidX > 995:
        kidX = 990
    elif kidX < 0:
        kidX = 2

    #Screen Block(Height)
    if kidY > 880:
        kidY = 879
        
    elif kidY < 0:
        kidY = 1

    #10 - Draw Screen Elements
    if state == STATE_START:
        window.fill(BLACK)
        playButton.draw()
        messageTextField.draw()
        messageTextField2.draw()
        
    elif state == STATE_GAME:
        window.blit(PUNCH_OUT, [0,0])
        kid.draw()
        healthText.draw()
        scoreText.draw()
        for index in range(0, N_SPIKES):
            spikeImgList[index].draw()
        for index in range(0, N_TYSON):
            tysonImgList[index].draw()

    elif state == STATE_RESULTS:
        window.blit(TYSON_WINS, [0,0])

    #11 - Update Screen
    pygame.display.update()

    #12 - Framerate
    clock.tick(FRAMES_PER_SECOND)

    
        
