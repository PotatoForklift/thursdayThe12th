from chars import *

floor1 = ['empty', 'event', 'empty', 'empty', 'fight', 'healing']
floor2 = ['empty', 'random', 'random', 'random', 'random', 'random', 'empty', 'fight', 'healing']
floor3 = ['empty', 'random', 'random', 'random', 'random', 'random', 'empty', 'fight', 'healing']
floor4 = ['empty', 'random', 'random', 'random', 'random', 'random', 'random', 'empty', 'fight', 'healing']
floor5 = ['healing', 'fight', 'fight', 'fight', 'THE END']

title = unimportAntSprites('sprites/buttons/title.png', [125, 50])

backgroundAnimation = ["sprites/bkg/background1.png", "sprites/bkg/background2.png", "sprites/bkg/background3.png",
                       "sprites/bkg/background4.png", "sprites/bkg/background5.png", "sprites/bkg/background6.png",
                       "sprites/bkg/background7.png", "sprites/bkg/background8.png"]
bkg1anim = ["Background7.png", "Background8.png"]




class background(pygame.sprite.Sprite):
    Count = 0
    
    def __init__(self, animation):
        super(background, self, ).__init__()
        self.surf = pygame.image.load(animation[0]).convert_alpha()
        # self.rect = self.surf.get_rect(center=(random.randint(-4, SCREENWIDTH - 2) + 21, 100))
        self.rect = self.surf.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.playerAnimation = animation
        self.time = 1
    
    def update(self):
        if self.Count == len(self.playerAnimation) - 1:
            self.Count = -1
        
        self.time += 1
        if self.time == 20:
            self.time = 0
            self.Count += 1
        
        self.surf = pygame.image.load(self.playerAnimation[self.Count]).convert_alpha()


back = background(backgroundAnimation)
bkg1 = background(bkg1anim)



def scene1emp():
    s1i1 = TextBIG("A camping trip to the woods has gone all wrong………………", (256, 100))
    s1i2 = TextBIG("    try to make your way out of the woods", (256, 140))
    s1i3 = TextBIG("       beware of what lurks in the night  : )", (256, 180))
    curLevelSprites.add(back, s1i1, s1i2, s1i3)


# the beginning instructions
# you have run out of water the group needs to aquire some before they perish
# your fire has burnt out, go collect firewood
# the healing rooms maybe get half of their total or lost hp back
#
