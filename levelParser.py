
levelFolder = './levels/'

def createLevelArray(moduleList):
    import os
    levelArray = []

    for filename in os.listdir(levelFolder):
        if filename.endswith('.lvl'):
            filePath = os.path.join(levelFolder, filename)
            with open(filePath) as f:
                rows = f.readlines()

            levelArray = [[item for item in row.split()] for row in rows]

            return createLevelSpriteGroup(levelArray, moduleList)
        else:
            continue


def createLevelSpriteGroup(lvlArray, moduleList):
    print(lvlArray)
    return 'meow'


