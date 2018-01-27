# Utility functions for reading in and parsing the stat sheets
# Author - William Theisen

import os, json

statsFolder = './stats/'

def readSheets():
    for filename in os.listdir(statsFolder):
        if filename.endswith('.stat'):
            filePath = os.path.join(statsFolder, filename)
            with open(filePath) as f:
                fileJSON = json.load(f)

            createClass(filePath, fileJSON)
        else:
            continue

def createClass(filePath, fileJSON):
    print('File path: ', filePath)
    print("File Contents:")

    classFileName = fileJSON["subtype"] + fileJSON["name"] + 'Class.py'
    classFile = open(classFileName, 'w')

    def writeLine(line):
        classFile.write(line)
        return

    writeLine('class ' + fileJSON["subtype"] + '():\n')
    writeLine('\tdef __init__(self):\n')
    writeLine('\t\tself.x = 0\n\t\tself.y=0\n')
    writeLine('\t\tself.image="' + fileJSON["imagePath"] + '"\n')
    writeLine('\t\tself.name="' + fileJSON['name'] + '"\n')

    if fileJSON["type"] == 'character':
        print("character type")
        writeLine('\t\tself.health="' + fileJSON['health'] + '"\n')
        writeLine('\t\tself.speed="' + fileJSON['speed'] + '"\n')
        writeLine('\t\tself.activeItem=None\n')
        writeLine('\t\tself.items=[]\n')
        writeLine('\n')
        writeLine('\tdef equipItem(self, item):\n')
        writeLine('\t\tself.items.append(item)\n')
        writeLine('\n')
        writeLine('\tdef move(self, xDir, yDir):\n')
        writeLine('\t\tself.x += self.speed * xDir\n')
        writeLine('\t\tself.y += self.speed * yDir\n')
        writeLine('\n')
        writeLine('\tdef useActiveItem(self):\n')
        writeLine('\t\tself.activeItem.use()\n')
        writeLine('\n')
    elif fileJSON["type"] == 'item':
        print("item type")
    elif fileJSON["type"] == 'environment':
        print("environment type")
        writeLine('\t\tself.destructable="' + fileJSON['destructable'] + '"\n')
        writeLine('\t\tself.items="' + fileJSON['contains'] + '"\n')
        writeLine('\t\tself.cover=' + fileJSON['cover'] + '\n')
        writeLine('\n')
        writeLine('\tdef equipItem(self, item):\n')
        writeLine('\t\tself.items.append(item)\n')
        writeLine('\n')
        writeLine('\tdef move(self, xDir, yDir):\n')
        writeLine('\t\tself.x += self.speed * xDir\n')
        writeLine('\t\tself.y += self.speed * yDir\n')
        writeLine('\n')
        writeLine('\tdef useActiveItem(self):\n')
        writeLine('\t\tself.activeItem.use()\n')
        writeLine('\n')

    writeLine('\tdef draw(self):\n')
    writeLine('\t\twindow.blit(self.image, (self.x, self.y))\n')
    writeLine('\n')

    classFile.close()

    return 1

readSheets()