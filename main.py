# Sam Fulbright, Ben Stevens, Kegan Acosta, Wyatt Lowe, Jack
# 4/12/24 - 5/10/24
# a game for the rumsey van
#
import random

import pygame.image

from scenes import *
import time


class FIRE(pygame.sprite.Sprite):
    Count = 0
    
    def __init__(self):
        super(FIRE, self).__init__()
        self.surf = pygame.image.load("sprites/fire/fire1.png").convert_alpha()
        # self.rect = self.surf.get_rect(center=(random.randint(-4, SCREENWIDTH - 2) + 21, 100))
        self.rect = self.surf.get_rect(center=(100, 525))
        self.playerAnimation = ["sprites/fire/fire1.png", "sprites/fire/fire2.png", "sprites/fire/fire3.png",
                                "sprites/fire/fire4.png"]
        self.time = 1
    
    def update(self):
        if self.Count == 3:
            self.Count = -1
        
        self.time += 1
        if self.time == 20:
            self.time = 0
            
            self.Count += 1
            
            
            yes
            
            medical monitering, put in water filtrations, money
            
            69000
            
            400$
            
            TIA
            
            7 years
            
            no
            
            2015
            
            671000000 six hundred seventy on mimllion
            
            they have higher standards for all of the chemicals 
            
            
        
        self.surf = pygame.image.load(self.playerAnimation[self.Count]).convert_alpha()


class charPick(pygame.sprite.Sprite):
    def __init__(self, image_file, location, person):
        super(charPick, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(image_file)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.mouse = False
        self.person = person
        self.selek = False
        self.count = 0
        self.startPos = location
    
    def update(self):
        if self.rect.bottom >= 0:
            self.rect.bottom = 90
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREENWIDTH:
            self.rect.right = SCREENWIDTH - 50
        if self.rect.top >= SCREENHEIGHT:
            self.rect = SCREENHEIGHT


def startPickScreen():
    pickCharScreenSprites.add(dogCharPick, kidCharPick, hikerCharPick, screenGirlCharPick, nerdCharPick, jockCharPick,
                              animalHippieCharPick, anxiousPersonCharPick)
    charScreenSprites.add(instructionTxt, instructionTxt2, selectionBlok, selPlyr1, selPlyr2, selPlyr3, selPlyr4,
                          basePlate1, basePlate2, basePlate3,
                          basePlate4, basePlate5, basePlate6, basePlate7,
                          basePlate8, dogTxt, dogTxtLabel, dogTxt2, dogTxt3, kidTxt, kidTxtLabel, kidTxt2, kidTxt3,
                          kidTxt4, hikerTxt, hikerTxt2, hikerTxt3, hikerTxt4, hikerTxtLabel,
                          skeenGielTxt, skeenGielTxt2, skeenGielTxt3, skeenGielTxt4, skeenGielTxt5, skeenGielTxt6,
                          skeenGielTxtLabel, nerdTxtLabel, nerdTxt, nerdTxt2, nerdTxt3, nerdTxt4, nerdTxt5, nerdTxt6,
                          nerdTxt7, nerdTxt8, jockTxtLabel, jockTxt, jockTxt2, jockTxt3, jockTxt4, jockTxt5, jockTxt6,
                          AnxPerTxtLabel, AnxPerTxt, AnxPerTxt2, AnxPerTxt3, AnxPerTxt4, AnxPerTxt4, AnxPerTxt5,
                          AnxPerTxt6, plantTxtLabel, plantTxt, plantTxt2, plantTxt3, plantTxt4, plantTxt5, plantTxt6,
                          continueButton)
    
    allSprites.add(charScreenSprites, pickCharScreenSprites)


def startGame():
    print(selp1)
    print(selp2)
    print(selp3)
    print(selp4)
    x = 167
    y = 60
    for spot in list:
        x -= 40
        y += 120
        
        if spot == 'kid':
            global kid
            kid = Kid([x, y])
            curLevelplayers.add(kid)
        
        if spot == 'dog':
            global dog
            dog = Dog([x, y])
            curLevelplayers.add(dog)
        
        if spot == 'hiker':
            global hiker
            hiker = Hiker([x, y])
            curLevelplayers.add(hiker)
        
        if spot == 'screenGirl':
            global screenGirl
            screenGirl = ScreenGirl([x, y])
            curLevelplayers.add(screenGirl)
        
        if spot == 'nerd':
            global nerd
            nerd = Nerd([x, y])
            curLevelplayers.add(nerd)
        
        if spot == 'jock':
            global jock
            jock = Jock([x, y])
            curLevelplayers.add(jock)
        
        if spot == 'animalHippie':
            global animalHippie
            animalHippie = AnimalHippie([x, y])
            curLevelplayers.add(animalHippie)
        
        if spot == 'anxiousPerson':
            global anx
            anx = AnxiousPerson([x, y])
            curLevelplayers.add(anx)
        night = nightCrawler((700, 300))
        curLevelEnemies.add(night)
    
    # one = unimportAntSprites("sprites/otherChars/hiker.png", [120, 30])
    # two = unimportAntSprites('sprites/otherChars/Nature Person.png', [90, 180])
    # three = unimportAntSprites('sprites/kid/kid1.png', [60, 300])
    # four = unimportAntSprites('sprites/otherChars/Nerd.png', [30, 420])
    # enem = unimportAntSprites('sprites/enemies/Fresco Nightcrawler.png', [500, 400])
    # curLevelSprites.add(one)
    # curLevelEnemies.add()
    # allSprites.add(one, two, three, four, enem)


def infoWin(per):
    # hi = unimportAntSprites("sprites/buttons/testInfo.png", [300, 100])
    # allSprites.add(hi)
    
    allSprites.remove(infoSprites)
    infoSprites.empty()
    
    if per.person == 'hiker':
        infoSprites.add(hikerI)
    if per.person == 'dog':
        infoSprites.add(dogI)
    if per.person == 'kid':
        infoSprites.add(kidI)
    if per.person == 'anxiousPerson':
        infoSprites.add(anxiousPersonI)
    if per.person == 'jock':
        infoSprites.add(jockI)
    if per.person == 'nerd':
        infoSprites.add(nerdI)
    if per.person == 'screenGirl':
        infoSprites.add(screenGirlI)
    if per.person == 'animalHippie':
        infoSprites.add(natureHippieI)
    
    infoSprites.add(xButton)
    allSprites.add(infoSprites)

def turn(char):

    hiker.buttons()
    allSprites.add(buttonsTurns)

##############################################################################
##############################################################################
hikerI = unimportAntSprites("sprites/info/hikerInfo.png", [300, 100])
dogI = unimportAntSprites("sprites/info/dogInfo.png", [300, 100])
kidI = unimportAntSprites("sprites/info/kidInfo.png", [300, 100])
anxiousPersonI = unimportAntSprites("sprites/info/anxiousPersonInfo.png", [300, 100])
jockI = unimportAntSprites("sprites/info/jockInfo.png", [300, 100])
nerdI = unimportAntSprites("sprites/info/nerdInfo.png", [300, 100])
screenGirlI = unimportAntSprites("sprites/info/screenGirlInfo.png", [300, 100])
natureHippieI = unimportAntSprites("sprites/info/natureHippieInfo.png", [300, 100])
xButton = unimportAntSprites("sprites/buttons/Xout.png", [865, 104])

instructionTxt = TextBIG("To select a character click and drag it into the boxes. To remove ", (200, 680))
instructionTxt2 = TextBIG("a character click on it. To see a characters stats left click.", (200, 700))

selPlyr1 = unimportAntSprites("sprites/characterSelect/selectionBlock.png", (46, 27), )
selp1 = 0
selPlyr2 = unimportAntSprites("sprites/characterSelect/selectionBlock.png", (46, 171), )
selp2 = 0
selPlyr3 = unimportAntSprites("sprites/characterSelect/selectionBlock.png", (46, 315), )
selp3 = 0
selPlyr4 = unimportAntSprites("sprites/characterSelect/selectionBlock.png", (46, 315 + 144), )
selp4 = 0

selectionBlok = unimportAntSprites("sprites/characterSelect/line.png", (30, 20 - 6), )

basePlate1 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (256 - 6, 20 - 6), )
dogTxtLabel = TextBIG("DOG", (256 + 130, 20 - 6))
dogTxt = Text("A faithful hound or a stray mutt, you’re", (256 + 130, 40 - 6))
dogTxt2 = Text("not sure which but this dog  is friendly", (256 + 130, 40 + 10))
dogTxt3 = Text("enough to come along on your trip.", (256 + 130, 40 + 26))

basePlate2 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (256 - 6, 180 - 6), )
kidTxtLabel = TextBIG("THE KID", (256 + 130, 180 - 6))
kidTxt = Text("You’re not sure whose kid this exactly is", (256 + 130, 195))
kidTxt2 = Text("but everyone seems happier to have", (256 + 130, 196 + 15))
kidTxt3 = Text("them around and not wandering the", (256 + 130, 212 + 15))
kidTxt4 = Text("woods alone. ", (256 + 130, 228 + 15))

basePlate3 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (256 - 6, 340 - 6), )
hikerTxtLabel = TextBIG("THE HIKER", (256 + 130, 340 - 6))
hikerTxt = Text("A lover of the outdoors with a strong", (256 + 130, 340 + 15))
hikerTxt2 = Text("back, good mind, and understanding of", (256 + 130, 356 + 15))
hikerTxt3 = Text("the outdoors. A jolly guy that is good ", (256 + 130, 372 + 15))
hikerTxt4 = Text("to have on every trip.", (256 + 130, 372 + 16 + 15))
#                 and knows all of your personal information.”

basePlate4 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (256 - 6, 500 - 6), )
skeenGielTxtLabel = TextBIG("THE SCREEN GIRL", (256 + 130, 500 - 6))
skeenGielTxt = Text("A girl obsessed with her phone. Only", (256 + 130, 500 + 15))
skeenGielTxt2 = Text("real reason she is going on this trip is", (256 + 130, 516 + 15))
skeenGielTxt3 = Text("because she saw a popular influencer", (256 + 130, 516 + 15 + 16))
skeenGielTxt4 = Text("going on one as well. She even brought", (256 + 130, 516 + 15 + 32))
skeenGielTxt5 = Text("a portable solar panel to charge her ", (256 + 130, 516 + 15 + 32 + 16))
skeenGielTxt6 = Text("phone.", (256 + 130, 516 + 15 + 32 + 32))

basePlate5 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (660 - 6, 20 - 6), )
AnxPerTxtLabel = TextBIG("THE ANXIOUS PERSON", (660 + 130, 20 - 6))
AnxPerTxt = Text("“AAAAAAAAAAAAAAAAAAAAAAAAA", (660 + 130, 20 + 16))
AnxPerTxt2 = Text("AAAAAAAAAAA” is how this person", (660 + 130, 20 + 32))
AnxPerTxt3 = Text("generally sounds. Scared by", (660 + 130, 20 + 32 + 16))
AnxPerTxt4 = Text("literally everything this person", (660 + 130, 20 + 64))
AnxPerTxt5 = Text("is a little on edge, which could be", (660 + 130, 20 + 80))
AnxPerTxt6 = Text("a good thing.", (660 + 130, 20 + 96))

basePlate6 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (660 - 6, 180 - 6), )
jockTxtLabel = TextBIG("JOCK", (660 + 130, 180 - 6))
jockTxt = Text("Your strong but simple minded ", (660 + 130, 200 - 6))
jockTxt2 = Text("stereotype of a Jock. Huge and Buff", (660 + 130, 200 + 10))
jockTxt3 = Text("but if a textbook was given you're,", (660 + 130, 200 + 26))
jockTxt4 = Text("not too sure that they would eat it", (660 + 130, 200 + 26 + 16))
jockTxt5 = Text("or rip it apart because they can’t", (660 + 130, 200 + 26 + 32))
jockTxt6 = Text("read.", (660 + 130, 200 + 26 + 48))

basePlate7 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (660 - 6, 340 - 6), )
plantTxtLabel = TextBIG("ANIMAL HIPPIE", (660 + 130, 340 - 6))
plantTxt = Text("Anything and Everything that is", (660 + 130, 360 - 6))
plantTxt2 = Text("outdoors this person loves. They", (660 + 130, 360 + 10))
plantTxt3 = Text("would eat moss…… MOSS! They", (660 + 130, 360 + 26))
plantTxt4 = Text("think every wolf and squirrel can be", (660 + 130, 360 + 26 + 16))
plantTxt5 = Text("tamed like they are a princess, but", (660 + 130, 360 + 26 + 32))
plantTxt6 = Text("you know the moss thing.", (660 + 130, 360 + 26 + 48))

basePlate8 = unimportAntSprites("sprites/characterSelect/pickBlock.png", (660 - 6, 500 - 6), )
nerdTxtLabel = TextBIG("NERD", (660 + 130, 500 - 6))
nerdTxt = Text("A dorkish person with knowledge", (660 + 130, 520 - 6))
nerdTxt2 = Text("of sci-fi and fantasy. Tabletop RPGs,", (660 + 130, 520 + 10))
nerdTxt3 = Text("comics, plants, medication, bugs,", (660 + 130, 520 + 26))
nerdTxt4 = Text("you name it they probably know", (660 + 130, 520 + 26 + 16))
nerdTxt5 = Text("about it. They’re not all that strong", (660 + 130, 520 + 26 + 32))
nerdTxt6 = Text("but with a broad knowledge of ", (660 + 130, 520 + 26 + 32 + 16))
nerdTxt7 = Text("almost any topic they’re not half", (660 + 130, 520 + 26 + 64))
nerdTxt8 = Text("bad to have along.", (660 + 130, 520 + 26 + 64 + 16))

dogCharPick = charPick("sprites/characterSelect/dogChar.png", (256, 20), 'dog')
kidCharPick = charPick("sprites/characterSelect/kidChar.png", (256, 180), 'kid')
hikerCharPick = charPick("sprites/characterSelect/hikerChar.png", (256, 340), 'hiker')
screenGirlCharPick = charPick("sprites/characterSelect/screenGirlChar.png", (256, 500), 'screenGirl')
anxiousPersonCharPick = charPick("sprites/characterSelect/anxiousPersonChar.png", (660, 20), 'anxiousPerson')
jockCharPick = charPick("sprites/characterSelect/jockChar.png", (660, 180), 'jock')
animalHippieCharPick = charPick("sprites/characterSelect/animalHippieChar.png", (660, 340), 'animalHippie')
nerdCharPick = charPick("sprites/characterSelect/nerdChar.png", (660, 500), 'nerd')

##############################################################
##############################################################


startButton = unimportAntSprites('sprites/buttons/startButton.png', [SCREENWIDTH / 2.4, SCREENHEIGHT / 2.4])
quitButton = unimportAntSprites('sprites/buttons/quitButton.png', [10, SCREENHEIGHT - 90])
title = unimportAntSprites('sprites/buttons/title.png', [125, 50])
continueButton = unimportAntSprites("sprites/buttons/continueButton.png", [SCREENWIDTH - 180, SCREENHEIGHT - 90])
arrowButton = unimportAntSprites("sprites/buttons/arrowButton2.png", [SCREENWIDTH - 100, SCREENHEIGHT - 90])
fire = FIRE()

startScreenSprites.add(startButton, title, fire)
allSprites.add(startButton, quitButton, title, fire)

SCREEN = 1
fires = True
hpBars = False
b = False
running = True
while running:
    if fires:
        fire.update()
    if b:
        back.update()
    try:
        print('hi')
        for pl in curLevelplayers:
            if pl.health >= 200:
                pl.health = 200
            if pl.health <= 0:
                pl.health = 0
        #for en in curLevelEnemies:


    except:
        print()
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if event.button == 1:
                if quitButton.rect.collidepoint(x, y):
                    running = False
                
                if startButton.rect.collidepoint(x, y) and SCREEN == 1:
                    allSprites.remove(startScreenSprites)
                    startPickScreen()
                    fires = False
                    SCREEN = 2
                if arrowButton.rect.collidepoint(x, y) and SCREEN == 3:
                    allSprites.remove(curLevelSprites, quitButton, arrowButton)
                    curLevelSprites.empty()
                    
                    allSprites.add(bkg1, curLevelplayers, curLevelEnemies, quitButton, arrowButton)
                    hpBars = True
                
                if continueButton.rect.collidepoint(x, y) and SCREEN == 2:
                    allSprites.remove(charScreenSprites, pickCharScreenSprites, )
                    # allSprites.add(selp1, selp2, selp3, selp4)
                    list = [selp1, selp2, selp3, selp4]
                    allSprites.remove(quitButton, continueButton)
                    scene1emp()
                    startGame()
                    
                    
                    SCREEN = 3
                    
                    allSprites.add(curLevelSprites, quitButton, arrowButton, )
                    b = True
                
                if xButton.rect.collidepoint(x, y):
                    allSprites.remove(infoSprites)
                
                for char in pickCharScreenSprites:
                    if char.rect.collidepoint(x, y) and SCREEN == 2:
                        char.mouse = True
                        char.selek = False
                try:
                    if Hiker([0, 0]).throwButton.rect.collidepoint((x, y)):
                        hiker.throw()
                        for en in curLevelEnemies:
                            en.health -=60
                        choicePlayer = []
                        for pl in curLevelplayers:
                            choicePlayer.append(pl)
                        charMinusHp = random.choice(choicePlayer)
                        charMinusHp.health -= 89
                    if Hiker([0, 0]).fstAidButton.rect.collidepoint((x, y)):
                        for pl in curLevelplayers:

                            pl.health += 30
                            if pl.health >= 200:
                                pl.health = 200
                            if pl.health<= 0:
                                curLevelplayers.remove(pl)
                                allSprites.remove(pl)

                    if Hiker([0, 0]).stickButton.rect.collidepoint((x, y)):
                        for en in curLevelEnemies:
                            en.health -= 80
                        choicePlayer = []
                        for pl in curLevelplayers:
                            choicePlayer.append(pl)
                        charMinusHp = random.choice(choicePlayer)



                except:
                    pass
                    
            
            if event.button == 3:
                for char in pickCharScreenSprites:
                    if char.rect.collidepoint(x, y):
                        per = char
                        infoWin(per)
            
        
        for char in pickCharScreenSprites:
            if event.type == MOUSEMOTION and char.mouse and not char.selek:
                char.rect.move_ip(event.rel)
            
            if event.type == MOUSEBUTTONUP and not char.selek:
                char.mouse = False
                char.rect.left, char.rect.top = char.startPos
            
            if char.rect.collidepoint(selPlyr1.rect.left + 30, selPlyr1.rect.centery):
                selp1 = char.person
                char.rect.center = selPlyr1.rect.center
                if char.count == 0:
                    char.selek = True
                    char.count = 1
            
            elif char.rect.collidepoint(selPlyr2.rect.left + 30, selPlyr2.rect.centery):
                selp2 = char.person
                char.rect.center = selPlyr2.rect.center
                if char.count == 0:
                    char.selek = True
                    char.count = 1
            
            elif char.rect.collidepoint(selPlyr3.rect.left + 30, selPlyr3.rect.centery):
                selp3 = char.person
                char.rect.center = selPlyr3.rect.center
                if char.count == 0:
                    char.selek = True
                    char.count = 1
            
            elif char.rect.collidepoint(selPlyr4.rect.left + 30, selPlyr4.rect.centery):
                selp4 = char.person
                char.rect.center = selPlyr4.rect.center
                if char.count == 0:
                    char.selek = True
                    char.count = 1
            else:
                char.count = 0
    screen.fill([0, 5, 20])
    
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)
    if hpBars:
        for char in curLevelplayers:
            char.draw_health(screen)
            turn(hiker)
        for en in curLevelEnemies:
            en.draw_health(screen)
    
    
    pygame.display.update()

pygame.quit()
