import pygame, math, utils
class  objectClass(pygame.sprite.Sprite):
    @staticmethod
    def getSubType():
        return player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y=100
        self.imagePath="./art/alien.png"
        self.src_image=pygame.image.load(self.imagePath)
        self.name="blonic"
        self.position= (self.x, self.y)
        print("import Successful")
        self.image=self.src_image
        self.rect=self.src_image.get_rect()
        self.objectID=0
        self.instanceID=0
        self.screen=None
        self.health=10
        self.speed=2
        self.activeItem=None
        self.items=[]

    def equipItem(self, item):
        self.items.append(item)

    def move(self, xDir, yDir):
        self.x += self.speed * xDir
        self.y += self.speed * yDir
        self.position = (self.x, self.y)
        self.rect.center = self.position
        if self.activeItem != None:
            self.activeItem.position = self.position

    def useActiveItem(self, sceneObjects):
        if self.activeItem == None:
            return
        self.activeItem.use(sceneObjects)

    def faceMouse(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        rotAngle = math.atan2(self.y - mouseY, mouseX - self.x)
        rotAngle = math.degrees(rotAngle)
        self.image = pygame.transform.rotate(self.src_image, rotAngle)
    def drawGEN(self):
        window.blit(self.image, (self.x, self.y))

def getSubType():    return "player"

