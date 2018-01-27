#utility functions for test.py
from collections import defaultdict

def createClasses():
    import sheetParser
    sheetParser.readSheets()

    return True

def importClasses():
    import os, imp

    temp = {}
    modules = defaultdict(list)

    classFolder = "./classes/"
    for filename in os.listdir(classFolder):
        if filename.endswith('.py'):
            pathname = os.path.join(classFolder, filename)
            print (pathname)
            print (filename)
            modName = filename.split('.')[0]
            #importlib.import_module(pathname.split(".")[0], package=filename.split(".")[0])
            temp[modName] = imp.load_source(modName, pathname)
            modules[temp[modName].getSubType()].append(temp[modName])

    return modules

def checkPointCol(x, y, sceneObjects):
    for key, val in sceneObjects.items():
        for obj in val:
            if obj.rect.collidepoint(x, y):
                if key == 'enemy':
                    obj.health -= 1
                    return True
            else:
                return True

    return False

def checkCol(startX, startY, endX, endY, sceneObjects):
    #figure out the line equation here
    m = (endY - startY) / (float)(endX - startX)
    b = startY - m * startX

    for x in range(startX, endX, 5):
        y = m * x + b
        if checkPointCol(x, y, sceneObjects):
            return

