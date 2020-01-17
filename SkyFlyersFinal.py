#importing libraries
import pygame
import sys
import random

#initialize pygame
pygame.init()

#Pipe variables
BottomPipeList = []
TopPipeList = []
pipeWidth = 70
pipeTimer = 0
pipeSpeed1 = 8
pipeSpeed2 = 15
pipeSpeed3 = 22

#score
score = 0

#screen width, height
screenHeight = 800
screenWidth = 1440

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sky Flyers")

#defining colours
red = (220, 20, 60)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#Main Variables
running = True
level1 = False
complete1 = False
level2 = False
complete2 = False
level3 = False
complete3 = False
ruleMenu = False
mainMenu = True
death = False
endless = False
LevelSelect = False


#Hero variables
heroX = 100
heroY = 250
heroWidth = 70
heroHeight = 50
vel = 7

#pipe variables
pipeHeight = random.randint(400, 600)
pipeRender = 1400

#Sound
pygame.mixer.music.load("music.mp3")  # background music taken from internet - see works cited
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

deathSound = pygame.mixer.Sound('deathSound.wav')   # death oof sound from internet - see works cited

winSound = pygame.mixer.Sound('win.wav')   # win sound - see works cited

pointSound = pygame.mixer.Sound('point.wav')



#Images
gameInstructions = pygame.image.load('game_instructions.png')  # custom instructions screen
bg = pygame.image.load('8-bit-wallpaper-28.png')    # background image from internet - see works cited
complete = pygame.image.load('complete.png')     # custom level completion screen
gameOverScreen = pygame.image.load('gameOver.png')     # custom gameover final screen

#sprites
plane = pygame.image.load('Plane.png')    # plane sprites taken from internet - see works cited
deadPlane = pygame.image.load('DeadPlane.png')    # dead plane sprites from internet - see works cited
bottomPipe = pygame.image.load('bottompipe.png')     # bottom pipe sprite from internet - see works cited
topPipe = pygame.image.load('toppipe.png')     # top pipe sprite from internet - see works cited



#Writing
startFont = pygame.font.SysFont("Arial", 90, True, True)
startFont.render("Sky Flyers", True, black)
chooseFont = pygame.font.SysFont("Arial", 70, True, False)
escapeFont = pygame.font.SysFont("Arial", 30, False, False)

chooseFont.render("Instructions", True, black)

#functions
def gameOver():

    deathFont = pygame.font.SysFont(None, 70, True, False)

    deathText = deathFont.render("Game Over", True, red)
    window.blit(deathText, (screenWidth // 2.5, screenHeight // 2.8))

    restartText = deathFont.render("Press B to Restart Level", True, red)
    window.blit(restartText, (screenWidth // 3.75, screenHeight // 2))

    scoreText = deathFont.render("Score: " + str(int(score)), True, red)
    window.blit(scoreText, (screenWidth // 2.38, screenHeight // 1.53))




#dynamic colours
Level1Colour = black
Level2Colour = black
Level3Colour = black
playTextColour = black
ruleTextColour = black
endlessTextColour = black

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    playDeathSound = True


#main menu
    if mainMenu:

#blitting text
        window.blit(bg, (0, 0))
        window.blit(startFont.render("Sky Flyers", True, black), (screenWidth // 2.7, screenHeight // 4.8))
        window.blit(chooseFont.render("Play", True, playTextColour), (screenWidth // 2.2, screenHeight // 2.8))
        window.blit(chooseFont.render("Instructions", True, ruleTextColour), (screenWidth // 2.629, screenHeight // 2))
        window.blit(chooseFont.render("Endless", True, endlessTextColour), (screenWidth // 2.38, screenHeight // 1.5))
        window.blit(escapeFont.render("By: John Balawejder & Judson Bell", True, black), (5, 5))

        score = 0

        mouse = pygame.mouse.get_pos()

#Check if the mouse is clicking the text
        if mouse[0] >= screenWidth // 2.2 and mouse[0] <= (screenWidth // 2.2) + 115 and mouse[1] > screenHeight // 2.8 and mouse[1] < (screenHeight // 2.8) + 40:

            if event.type == pygame.MOUSEBUTTONUP:
                mainMenu, LevelSelect = False, True
            playTextColour = blue
        else:                   #makes text blue if you are hovering over it
            playTextColour = black

        if mouse[0] >= screenWidth // 2.629 and mouse[0] <= (screenWidth // 2.629) + 340 and mouse[1] > screenHeight // 2 and mouse[1] < (screenHeight // 2) + 40:

            if event.type == pygame.MOUSEBUTTONUP:
                mainMenu, ruleMenu = False, True
            ruleTextColour = blue
        else:                       #makes text blue if you are hovering over it
            ruleTextColour = black

        if mouse[0] >= screenWidth // 2.38 and mouse[0] <= (screenWidth // 2.38) + 210 and mouse[1] > screenHeight // 1.5 and mouse[1] < (screenHeight // 1.5) + 40:

            if event.type == pygame.MOUSEBUTTONUP:
                mainMenu, endless = False, True
            endlessTextColour = blue
        else:                           #makes text blue if you are hovering over it
            endlessTextColour = black


    if LevelSelect:
#blitting Text
        window.blit(bg, (0, 0))
        window.blit(startFont.render("Level Select", True, black), (screenWidth // 2.8, screenHeight // 4.9))
        window.blit(chooseFont.render("Level 1", True, Level1Colour), (screenWidth // 2.3, screenHeight // 2.8))
        window.blit(chooseFont.render("Level 2", True, Level2Colour), (screenWidth // 2.3, screenHeight // 2))
        window.blit(chooseFont.render("Level 3", True, Level3Colour), (screenWidth // 2.3, screenHeight // 1.551))
        window.blit(escapeFont.render("Press ESC to Return", True, black), (10, 10))

        mouse = pygame.mouse.get_pos()

        BottomPipeList = []             #resets the pipes and player position
        heroY = 250
        death = False

#Checking if text has been pressed

        if mouse[0] >= screenWidth // 2.3 and mouse[0] <= (screenWidth // 2.3) + 190 and mouse[1] >= screenHeight // 2.8 and mouse[1] <= (screenHeight // 2.8) + 50:
            if event.type == pygame.MOUSEBUTTONDOWN:
                LevelSelect, mainMenu, level1 = False, False, True
            Level1Colour = blue
        else:                       #makes text blue if you are hovering over it
            Level1Colour = black

        if mouse[0] >= screenWidth // 2.3 and mouse[0] <= (screenWidth // 2.3) + 190 and mouse[1] >= screenHeight // 2 and mouse[1] <= (screenHeight // 2) + 50:
            if event.type == pygame.MOUSEBUTTONDOWN:
                LevelSelect, mainMenu, level2 = False, False, True
            Level2Colour = blue
        else:                       #makes text blue if you are hovering over it
            Level2Colour = black

        if mouse[0] >= screenWidth // 2.3 and mouse[0] <= (screenWidth // 2.3) + 190 and mouse[1] >= screenHeight // 1.551 and mouse[1] <= (screenHeight // 1.551) + 50:
            if event.type == pygame.MOUSEBUTTONDOWN:
                LevelSelect, mainMenu, level3 = False, False, True
            Level3Colour = blue
        else:                       #makes text blue if you are hovering over it
            Level3Colour = black

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:            #checks to see if esc is pressed
                    LevelSelect, mainMenu = False, True

#rule menu
    if ruleMenu:

        window.blit(gameInstructions, (0, 0))       #blits the game instruction screen


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ruleMenu, mainMenu = False, True

#main game

    if level1:          #first level of main game

        pygame.time.delay(1)

        window.blit(bg, (0, 0))
        window.blit(escapeFont.render("Score: " + str(score) + "/15", True, black), (1300, 10))
        window.blit(escapeFont.render("Press ESC to Return", True, black), (10, 10))

#movement
        if not death:

            pipeSpeed1 = 15     #sets pipe speed

            if keys[pygame.K_UP] and heroY > screenHeight - heroHeight - vel:
                heroY -= vel

            if heroY < screenHeight - heroHeight - vel:
                heroY += 5
                window.blit(plane, (heroX - 12, heroY - 15))

            elif heroY == pipeHeight:
                death = True

            else:
                pipeSpeed1 = 0
                death = True

            if keys[pygame.K_SPACE]:
                heroY -= 10

#Pipes

            if pipeTimer >= 43:     # X         Y for pipe timer
                BottomPipeList.append([1400, random.randint(400, 600)])


        for i in BottomPipeList:

            i[0] -= pipeSpeed1

#checking for collision/death
            if heroY + heroHeight >= i[1] and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroY <= i[1] - 200 and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroX >= i[0] + pipeWidth // 2 - 3 and heroX <= i[0] + pipeWidth // 2 + 3:
                score += 1
                pointSound.play()

            #drawing the pipes
            window.blit(bottomPipe, (i[0], i[1]))
            window.blit(topPipe, (i[0], i[1] - 800))

        pipeTimer += 1

        if pipeTimer >= 44:
            pipeTimer = 0

        if keys[pygame.K_ESCAPE]:
            level1, mainMenu = False, True

#resetting the plane for retry
        if death:
            window.blit(deadPlane, (heroX - 12, heroY - 10))
            pipeSpeed1 = 0
            gameOver()
            if keys[pygame.K_b]:
                BottomPipeList = []
                heroY = 250
                score = 0
                death, level1 = False, True

        if score == 15:
            level1, complete1 = False, True

    if complete1:

#displays levle 1 completion screen
        window.blit(complete, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                complete1, level1, mainMenu = False, False, True

        if keys[pygame.K_n]:
            BottomPipeList = []
            heroY = 250
            score = 15
            complete1, level2 = False, True


#Level 2
    if level2:

        pygame.time.delay(1)

        window.blit(bg, (0, 0))
        window.blit(escapeFont.render("Score: " + str(score) + "/30", True, black), (1300, 10))
        window.blit(escapeFont.render("Press ESC to Return", True, black), (10, 10))

        pipeWidth = 70

# movement
        if not death:

            pipeSpeed2 = 22

            if keys[pygame.K_UP] and heroY > screenHeight - heroHeight - vel:
                heroY -= vel

            if heroY < screenHeight - heroHeight - vel:
                heroY += 5
                window.blit(plane, (heroX - 12, heroY - 15))

            elif heroY == pipeHeight:
                death = True

            else:
                pipeSpeed2 = 0
                death = True

            if keys[pygame.K_SPACE]:
                heroY -= 10
# Pipes

            if pipeTimer >= 40:  # X         Y
                BottomPipeList.append([1400, random.randint(400, 600)])

        for i in BottomPipeList:
            i[0] -= pipeSpeed2

            # checking for collision/death
            if heroY + heroHeight >= i[1] and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroY <= i[1] - 200 and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()


            elif heroX >= i[0] + pipeWidth // 2 - 7 and heroX <= i[0] + pipeWidth // 2 + 7:
                score += 1
                pointSound.play()


            window.blit(bottomPipe, (i[0], i[1]))
            window.blit(topPipe, (i[0], i[1] - 800))

        pipeTimer += 1

        if pipeTimer >= 41:
            pipeTimer = 0

        if keys[pygame.K_ESCAPE]:
            level2, mainMenu = False, True

        if death:

            window.blit(deadPlane, (heroX - 12, heroY - 10))
            gameOver()
            pipeSpeed2 = 0
            if keys[pygame.K_b]:
                BottomPipeList = []
                score = 15
                heroY = 250
                death, level2 = False, True


        if score == 30:
            level2, complete2 = False, True


    if complete2:

        window.blit(complete, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                complete2, level2, mainMenu = False, False, True

        if keys[pygame.K_n]:
            BottomPipeList = []
            heroY = 250
            complete2, level3 = False, True


    if level3:

        pygame.time.delay(1)


        window.blit(bg, (0, 0))
        window.blit(escapeFont.render("Score: " + str(int(score)) + "/50", True, black), (1300, 10))
        window.blit(escapeFont.render("Press ESC to Return", True, black), (10, 10))



# movement
        if not death:

            pipeSpeed3 = 30

            if keys[pygame.K_UP] and heroY > screenHeight - heroHeight - vel:
                heroY -= vel

            if heroY < screenHeight - heroHeight - vel:
                heroY += 5
                window.blit(plane, (heroX - 12, heroY - 15))

            elif heroY == pipeHeight:
                death = True

            else:
                pipeSpeed3 = 0
                death = True

            if keys[pygame.K_SPACE]:
                heroY -= 10
 # Pipes

            if pipeTimer >= 25:  # X         Y
                BottomPipeList.append([1400, random.randint(400, 600)])

        for i in BottomPipeList:
            i[0] -= pipeSpeed3

     # checking for collision/death
            if heroY + heroHeight >= i[1] and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroY <= i[1] - 200 and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroX >= i[0] + pipeWidth // 2 - 15 and heroX <= i[0] + pipeWidth // 2 + 15:
                score += .5
                pointSound.play()


            window.blit(bottomPipe, (i[0], i[1]))
            window.blit(topPipe, (i[0], i[1] - 800))

        pipeTimer += 1

        if pipeTimer >= 26:
            pipeTimer = 0

        if keys[pygame.K_ESCAPE]:
            level3, mainMenu = False, True

        if death:
            window.blit(deadPlane, (heroX - 12, heroY - 10))
            gameOver()
            pipeSpeed3 = 0
            if keys[pygame.K_b]:
                BottomPipeList = []
                heroY = 250
                score = 30
                death, level3 = False, True

        if score == 50:
            level3, complete3 = False, True

    if complete3:

        window.blit(gameOverScreen, (0, 0))
        winSound.play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                complete3, level3, mainMenu = False, False, True

        if keys[pygame.K_n]:
            BottomPipeList = []
            heroY = 250
            score = 0
            complete3, LevelSelect = False, True

    if endless:
        pygame.time.delay(1)

        window.blit(bg, (0, 0))
        window.blit(escapeFont.render("Score: " + str(int(score)), True, black), (1300, 10))
        window.blit(escapeFont.render("Press ESC to Return", True, black), (10, 10))



        # movement
        if not death:

            pipeSpeed3 = 30

            if keys[pygame.K_UP] and heroY > screenHeight - heroHeight - vel:
                heroY -= vel

            if heroY < screenHeight - heroHeight - vel:
                heroY += 5
                window.blit(plane, (heroX - 12, heroY - 15))

            elif heroY == pipeHeight:
                death = True

            else:
                pipeSpeed3 = 0
                death = True

            if keys[pygame.K_SPACE]:
                heroY -= 10
                # Pipes

            if pipeTimer >= 25:  # X         Y
                BottomPipeList.append([1400, random.randint(400, 600)])

        for i in BottomPipeList:
            i[0] -= pipeSpeed3

 # checking for collision/death
            if heroY + heroHeight >= i[1] and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroY <= i[1] - 200 and heroX + heroWidth >= i[0] and heroX + heroWidth <= i[0] + pipeWidth:
                death = True
                deathSound.play()

            elif heroX >= i[0] + pipeWidth // 2 - 15 and heroX <= i[0] + pipeWidth // 2 + 15:
                score += .5
                pointSound.play()
#blitting pipes to screen
            window.blit(bottomPipe, (i[0], i[1]))
            window.blit(topPipe, (i[0], i[1] - 800))

        pipeTimer += 1

        if pipeTimer >= 26:
            pipeTimer = 0

        if keys[pygame.K_ESCAPE]:
            endless, mainMenu = False, True

        if death:
            window.blit(deadPlane, (heroX - 12, heroY - 10))
            gameOver()
            pipeSpeed3 = 0
            if keys[pygame.K_b]:
                BottomPipeList = []
                heroY = 250
                score = 0
                death, endless = False, True


    pygame.display.update()
    window.fill(white)
sys.exit()
