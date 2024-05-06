# the characters and enemies

from base import *


def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+1, pos[1]+1)
    innerSize = ((size[0]-2) * progress, size[1]-2)
    rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
    pygame.draw.rect(surf, healthC, rect)

class Dog(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(Dog, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/dog/dog1.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 120
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 10), (0, 255, 0), self.health / max_health)


class Kid(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(Kid, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/kid/kid1.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class Hiker(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(Hiker, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/hiker.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.health = 200
        
        self.throwButtonSurf = pygame.image.load("sprites/buttons/hkrThrwEquipBttn.png").convert_alpha()
        self.throwButtonRect = self.throwButtonSurf.get_rect(center=(400, 300))
        
        self.stickButtonSurf = pygame.image.load("sprites/buttons/hkrWlkngStkBttn.png").convert_alpha()
        self.stickButtonRect = self.stickButtonSurf.get_rect(center = (400, 400))
        
        self.labelSurf = pygame.image.load("sprites/buttons/hkrTrnLbl.png")
        self.labelRect = self.labelSurf.get_rect(center = (400, 120))
        
        self.firstAidSurf = pygame.image.load("sprites/buttons/hkrFrstAidBttn.png")
        self.firstAidSurf = self.labelSurf.get_rect(center = (400, 500))
        
        
    
    def update(self):
        pass
        #if self.moveCount == 3:
        #    self.moveCount = -1

        
        #self.weTime += 1
        #self.surf = pygame.image.load(self.playerAnimation[self.moveCount]).convert_alpha()
        # print(self.moveCount)
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)
        
    def buttons(self):
        screen.blit(self.throwButtonSurf, self.throwButtonRect)
        screen.blit(self.stickButtonSurf, self.stickButtonRect)
        screen.blit(self.labelSurf, self.labelRect)
        
    def throw(self):
        self.rect.left, self.rect.top = (500, 500)
        print('hi')
        
        


class ScreenGirl(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(ScreenGirl, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/ScreenGirl.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class AnxiousPerson(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(AnxiousPerson, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/anxiousPerson.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class Jock(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(Jock, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/jock.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class AnimalHippie(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(AnimalHippie, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/natureHippie.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class Nerd(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(Nerd, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/otherChars/Nerd.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)


class nightCrawler(pygame.sprite.Sprite):
    def __init__(self, location, ):
        super(nightCrawler, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("sprites/enemies/Fresco Nightcrawler2.png")
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        self.startPos = location
        self.health = 200
    
    def update(self):
        pass
    
    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.surf.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = 200
        draw_health_bar(surf, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)
