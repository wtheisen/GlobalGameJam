import pygame, math, utils
class  objectClass(pygame.sprite.Sprite):
    @staticmethod
    def getSubType():
        return wall
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y=100
        self.imagePath="./art/wall.png"
        self.src_image=pygame.image.load(self.imagePath)
        self.name="wall"
        self.position= (self.x, self.y)
        print("import Successful")
        self.image=self.src_image
        self.rect=self.src_image.get_rect()
        self.objectID=0
        self.instanceID=0
        self.screen=None
        self.destructable=True
        self.items=[credits]
        self.cover=1
        self.health=5

    def equipItem(self, item):
        self.items.append(item)

    def move(self, xDir, yDir):
        self.x += self.speed * xDir
        self.y += self.speed * yDir

    def useActiveItem(self):
        self.activeItem.use()

    def drawGEN(self):
        window.blit(self.image, (self.x, self.y))

def getSubType():    return "wall"

