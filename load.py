'''
this file will handle loading the map, images, and sounds

TO DO:
load textures (TP2/3)
load sounds (TP3)
'''

from pyglet import *

# loads a map from the mapID
def loadMap(mapID):
    flipMap = []
    mapLoader = resource.Loader(['levels'])
    # open map file
    fileName = mapID + '.txt'
    mapFile = mapLoader.file(fileName, 'r')
    # loop through each row
    for rowText in mapFile:
        textRow = rowText.strip().split()
        # loop through each col
        mapRow = []
        for i in range(len(textRow)):
            # cast string to int and add to list
            mapRow.append(int(textRow[i]))
        flipMap.append(mapRow)
    
    # reverse map (so pos can be indexed by x,y)
    map = []
    rows, cols = len(flipMap), len(flipMap[0])
    for col in range(cols):
        colList = [flipMap[row][col] for row in range(rows)]
        map.append(colList)
    return map

def loadTextures():
    texLoader = resource.Loader(['textures'])
    texFileNames = ['bookshelf', 'gray_bricks', 'planks', 'stone_floor',
                    'stone_tile', 'stone', 'wall_bricks']
    texList = []
    for fileName in texFileNames:
        tex = texLoader.texture(fileName + '.png')
        texList.append(tex)
    return texList

def loadSprites():
    spriteLoader = resource.Loader(['sprites'])
    spriteFileNames = ['bone_shield', 'death_speaker', 'druid', 'shadow_soul',
                       'shadow_tendrils', 'skeleton', 'zombie', 'sword']
    spriteList = []
    for fileName in spriteFileNames:
        spriteFile = spriteLoader.image(fileName + '.png')
        spriteList.append(spriteFile)
    return spriteList

def loadSFX():
    sfxLoader = resource.Loader(['sfx'])
    sfxFileNames = ['footstep', 'enemy_snarl', 'enemy_death', 'button_hover',
                    'button_press', 'pause', 'unpause', 'sword_attack', 'enemy_hit',
                    'player_death', 'player_damage'] 
    sfxList = []
    for fileName in sfxFileNames:
        fullFileName = fileName + '.mp3'
        sfxFile = sfxLoader.media(fullFileName, streaming=False)
        sfxList.append(sfxFile)
    return sfxList

def loadMusic():
    musicLoader = resource.Loader(['music'])
    musicFileNames = ['death_music', 'win_music'] 
    trackList = []
    for fileName in musicFileNames:
        fullFileName = fileName + '.mp3'
        musicFile = musicLoader.media(fullFileName)
        trackList.append(musicFile)
    return trackList