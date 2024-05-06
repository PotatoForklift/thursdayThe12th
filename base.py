# basic vars and imports maybe needed, maybe not
#

import pygame
from pygame.locals import *

pygame.font.init()
from pygame.constants import *

from pygame.constants import MOUSEMOTION, MOUSEBUTTONUP
# from pytmx import load_pygame
import random

# import pytmx

current = ''
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1010, 700), pygame.FULLSCREEN)
SCREENWIDTH = screen.get_width()
SCREENHEIGHT = screen.get_height()
start = True
font = pygame.font.Font(None, 30)

startScreenSprites = pygame.sprite.Group()

pickCharScreenSprites = pygame.sprite.Group()
charScreenSprites = pygame.sprite.Group()

infoSprites = pygame.sprite.Group()


curLevelSprites = pygame.sprite.Group()
curLevelEnemies = pygame.sprite.Group()
curLevelplayers = pygame.sprite.Group()

allSprites = pygame.sprite.Group()



class Text(pygame.sprite.Sprite):
    def __init__(self, txt, loc):
        pygame.sprite.Sprite.__init__(self, )
        self.text = txt
        self.font = pygame.font.Font(None, 20)
        self.surf = self.font.render(self.text, False, [204, 103, 55])
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = loc


class TextBIG(pygame.sprite.Sprite):
    def __init__(self, txt, loc):
        pygame.sprite.Sprite.__init__(self, )
        self.text = txt
        self.font = pygame.font.Font(None, 30)
        self.surf = self.font.render(self.text, False, [204, 153, 55])
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = loc

class unimportAntSprites(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(image_file)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location

################################################################
# startButton = pygame.transform.scale(startButton.image, (startButton.rect.width*2, startButton.rect.height*2))
