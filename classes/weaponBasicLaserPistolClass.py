import pygame, math, utils
class  objectClass(pygame.sprite.Sprite):
    @staticmethod
    def getSubType():
        return weapon
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y=100
        self.imagePath="./art/alien.png"
        self.src_image=pygame.image.load(self.imagePath)
        self.name="BasicLaserPistol"
        self.position= (self.x, self.y)
        print("import Successful")
        self.image=self.src_image
        self.rect=self.src_image.get_rect()
        self.objectID=0
        self.instanceID=0
        self.screen=None
        self.weaponType="ranged"
        self.consumable=0
        self.ammo=-1
        self.damage=1
        self.effects=[]

    def use(self, sceneObjects):
        print("used item")
        self.addEffect(sceneObjects)

    def addEffect(self, sceneObjects):
        print("drawing a light line")
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x, self.y = self.position
        deltaX = mouseX -self.x
        deltaY = mouseY -self.y
        screenY = self.screen.get_height()
        while (mouseY < screenY) and (mouseY > 0):
            mouseY +=deltaY
            mouseX +=deltaX
        pygame.draw.line(self.screen, (200,200,200), self.position, (mouseX,mouseY), 9)
        utils.checkCol(self.x, self.y, mouseX, mouseY, sceneObjects)
    def drawGEN(self):
        window.blit(self.image, (self.x, self.y))

def getSubType():    return "weapon"

