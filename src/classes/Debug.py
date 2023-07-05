from pyboy.utils import WindowEvent
import logging
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
import src.classes.PokemonData as pokemonData
import numpy
import PIL
import os
import json
import pyboy

class Debug:
    def SpriteFarm(session):
        outputPath = 'Debug\\SpriteFarm\\Spritefarm.txt'
        file = open(outputPath, 'w')
        file.close()
        file = open(outputPath, 'a')

        # Farm sprite0
        sprite00 = session.botsupport_manager().sprite(0)
        sprite01 = session.botsupport_manager().sprite(1)
        sprite02 = session.botsupport_manager().sprite(2)
        sprite03 = session.botsupport_manager().sprite(3)

        sprite00TileId = sprite00.tiles[0].tile_identifier
        sprite00Tile = session.botsupport_manager().tile(sprite00TileId).image_ndarray()

        sprite01TileId = sprite01.tiles[0].tile_identifier
        sprite01Tile = session.botsupport_manager().tile(sprite01TileId).image_ndarray()

        sprite02TileId = sprite02.tiles[0].tile_identifier
        sprite02Tile = session.botsupport_manager().tile(sprite02TileId).image_ndarray()
       
        sprite03TileId = sprite03.tiles[0].tile_identifier
        sprite03Tile = session.botsupport_manager().tile(sprite03TileId).image_ndarray()
       
        sprite00TopHalf = numpy.concatenate((sprite00Tile, sprite01Tile), axis=1)
        sprite00BottomHalf = numpy.concatenate((sprite02Tile, sprite03Tile), axis=1)
        sprite00Full = numpy.concatenate((sprite00TopHalf, sprite00BottomHalf), axis=0)

        sprite00FullPIL = PIL.Image.fromarray(sprite00Full)
        sprite00FullPIL.save('Debug\\SpriteFarm\\sprite00.png')

        # Farm sprite1
        sprite10 = session.botsupport_manager().sprite(4)
        sprite11 = session.botsupport_manager().sprite(5)
        sprite12 = session.botsupport_manager().sprite(6)
        sprite13 = session.botsupport_manager().sprite(7)

        sprite10TileId = sprite10.tiles[0].tile_identifier
        sprite10Tile = session.botsupport_manager().tile(sprite10TileId).image_ndarray()

        sprite11TileId = sprite11.tiles[0].tile_identifier
        sprite11Tile = session.botsupport_manager().tile(sprite11TileId).image_ndarray()

        sprite12TileId = sprite12.tiles[0].tile_identifier
        sprite12Tile = session.botsupport_manager().tile(sprite12TileId).image_ndarray()
       
        sprite13TileId = sprite13.tiles[0].tile_identifier
        sprite13Tile = session.botsupport_manager().tile(sprite13TileId).image_ndarray()
       
        sprite10TopHalf = numpy.concatenate((sprite10Tile, sprite11Tile), axis=1)
        sprite10BottomHalf = numpy.concatenate((sprite12Tile, sprite13Tile), axis=1)
        sprite10Full = numpy.concatenate((sprite10TopHalf, sprite10BottomHalf), axis=0)

        sprite10FullPIL = PIL.Image.fromarray(sprite10Full)
        sprite10FullPIL.save('Debug\\SpriteFarm\\sprite10.png')

        # Farm sprite2
        sprite20 = session.botsupport_manager().sprite(8)
        sprite21 = session.botsupport_manager().sprite(9)
        sprite22 = session.botsupport_manager().sprite(10)
        sprite23 = session.botsupport_manager().sprite(11)

        sprite20TileId = sprite20.tiles[0].tile_identifier
        sprite20Tile = session.botsupport_manager().tile(sprite20TileId).image_ndarray()

        sprite21TileId = sprite21.tiles[0].tile_identifier
        sprite21Tile = session.botsupport_manager().tile(sprite21TileId).image_ndarray()

        sprite22TileId = sprite22.tiles[0].tile_identifier
        sprite22Tile = session.botsupport_manager().tile(sprite22TileId).image_ndarray()
       
        sprite23TileId = sprite23.tiles[0].tile_identifier
        sprite23Tile = session.botsupport_manager().tile(sprite23TileId).image_ndarray()
       
        sprite20TopHalf = numpy.concatenate((sprite20Tile, sprite21Tile), axis=1)
        sprite20BottomHalf = numpy.concatenate((sprite22Tile, sprite23Tile), axis=1)
        sprite20Full = numpy.concatenate((sprite20TopHalf, sprite20BottomHalf), axis=0)

        sprite20FullPIL = PIL.Image.fromarray(sprite20Full)
        sprite20FullPIL.save('Debug\\SpriteFarm\\sprite20.png')

        # Farm sprite3
        sprite30 = session.botsupport_manager().sprite(12)
        sprite31 = session.botsupport_manager().sprite(13)
        sprite32 = session.botsupport_manager().sprite(14)
        sprite33 = session.botsupport_manager().sprite(15)

        sprite30TileId = sprite30.tiles[0].tile_identifier
        sprite30Tile = session.botsupport_manager().tile(sprite30TileId).image_ndarray()

        sprite31TileId = sprite31.tiles[0].tile_identifier
        sprite31Tile = session.botsupport_manager().tile(sprite31TileId).image_ndarray()

        sprite32TileId = sprite32.tiles[0].tile_identifier
        sprite32Tile = session.botsupport_manager().tile(sprite32TileId).image_ndarray()
       
        sprite33TileId = sprite33.tiles[0].tile_identifier
        sprite33Tile = session.botsupport_manager().tile(sprite33TileId).image_ndarray()
       
        sprite30TopHalf = numpy.concatenate((sprite30Tile, sprite31Tile), axis=1)
        sprite30BottomHalf = numpy.concatenate((sprite32Tile, sprite33Tile), axis=1)
        sprite30Full = numpy.concatenate((sprite30TopHalf, sprite30BottomHalf), axis=0)

        sprite30FullPIL = PIL.Image.fromarray(sprite30Full)
        sprite30FullPIL.save('Debug\\SpriteFarm\\sprite30.png')

        # Farm sprite4
        sprite40 = session.botsupport_manager().sprite(16)
        sprite41 = session.botsupport_manager().sprite(17)
        sprite42 = session.botsupport_manager().sprite(18)
        sprite43 = session.botsupport_manager().sprite(19)

        sprite40TileId = sprite40.tiles[0].tile_identifier
        sprite40Tile = session.botsupport_manager().tile(sprite40TileId).image_ndarray()

        sprite41TileId = sprite41.tiles[0].tile_identifier
        sprite41Tile = session.botsupport_manager().tile(sprite41TileId).image_ndarray()

        sprite42TileId = sprite42.tiles[0].tile_identifier
        sprite42Tile = session.botsupport_manager().tile(sprite42TileId).image_ndarray()
       
        sprite43TileId = sprite43.tiles[0].tile_identifier
        sprite43Tile = session.botsupport_manager().tile(sprite43TileId).image_ndarray()
       
        sprite40TopHalf = numpy.concatenate((sprite40Tile, sprite41Tile), axis=1)
        sprite40BottomHalf = numpy.concatenate((sprite42Tile, sprite43Tile), axis=1)
        sprite40Full = numpy.concatenate((sprite40TopHalf, sprite40BottomHalf), axis=0)

        sprite40FullPIL = PIL.Image.fromarray(sprite40Full)
        sprite40FullPIL.save('Debug\\SpriteFarm\\sprite40.png')

        # Farm sprite5
        sprite50 = session.botsupport_manager().sprite(20)
        sprite51 = session.botsupport_manager().sprite(21)
        sprite52 = session.botsupport_manager().sprite(22)
        sprite53 = session.botsupport_manager().sprite(23)

        sprite50TileId = sprite50.tiles[0].tile_identifier
        sprite50Tile = session.botsupport_manager().tile(sprite50TileId).image_ndarray()

        sprite51TileId = sprite51.tiles[0].tile_identifier
        sprite51Tile = session.botsupport_manager().tile(sprite51TileId).image_ndarray()

        sprite52TileId = sprite52.tiles[0].tile_identifier
        sprite52Tile = session.botsupport_manager().tile(sprite52TileId).image_ndarray()
       
        sprite53TileId = sprite53.tiles[0].tile_identifier
        sprite53Tile = session.botsupport_manager().tile(sprite53TileId).image_ndarray()
       
        sprite50TopHalf = numpy.concatenate((sprite50Tile, sprite51Tile), axis=1)
        sprite50BottomHalf = numpy.concatenate((sprite52Tile, sprite53Tile), axis=1)
        sprite50Full = numpy.concatenate((sprite50TopHalf, sprite50BottomHalf), axis=0)

        sprite50FullPIL = PIL.Image.fromarray(sprite50Full)
        sprite50FullPIL.save('Debug\\SpriteFarm\\sprite50.png')

        # Farm sprite6
        sprite60 = session.botsupport_manager().sprite(24)
        sprite61 = session.botsupport_manager().sprite(25)
        sprite62 = session.botsupport_manager().sprite(26)
        sprite63 = session.botsupport_manager().sprite(27)

        sprite60TileId = sprite60.tiles[0].tile_identifier
        sprite60Tile = session.botsupport_manager().tile(sprite60TileId).image_ndarray()

        sprite61TileId = sprite61.tiles[0].tile_identifier
        sprite61Tile = session.botsupport_manager().tile(sprite61TileId).image_ndarray()

        sprite62TileId = sprite62.tiles[0].tile_identifier
        sprite62Tile = session.botsupport_manager().tile(sprite62TileId).image_ndarray()
       
        sprite63TileId = sprite63.tiles[0].tile_identifier
        sprite63Tile = session.botsupport_manager().tile(sprite63TileId).image_ndarray()
       
        sprite60TopHalf = numpy.concatenate((sprite60Tile, sprite61Tile), axis=1)
        sprite60BottomHalf = numpy.concatenate((sprite62Tile, sprite63Tile), axis=1)
        sprite60Full = numpy.concatenate((sprite60TopHalf, sprite60BottomHalf), axis=0)

        sprite60FullPIL = PIL.Image.fromarray(sprite60Full)
        sprite60FullPIL.save('Debug\\SpriteFarm\\sprite60.png')

        # Farm sprite7
        sprite70 = session.botsupport_manager().sprite(28)
        sprite71 = session.botsupport_manager().sprite(29)
        sprite72 = session.botsupport_manager().sprite(30)
        sprite73 = session.botsupport_manager().sprite(31)

        sprite70TileId = sprite70.tiles[0].tile_identifier
        sprite70Tile = session.botsupport_manager().tile(sprite70TileId).image_ndarray()

        sprite71TileId = sprite71.tiles[0].tile_identifier
        sprite71Tile = session.botsupport_manager().tile(sprite71TileId).image_ndarray()

        sprite72TileId = sprite72.tiles[0].tile_identifier
        sprite72Tile = session.botsupport_manager().tile(sprite72TileId).image_ndarray()
       
        sprite73TileId = sprite73.tiles[0].tile_identifier
        sprite73Tile = session.botsupport_manager().tile(sprite73TileId).image_ndarray()
       
        sprite70TopHalf = numpy.concatenate((sprite70Tile, sprite71Tile), axis=1)
        sprite70BottomHalf = numpy.concatenate((sprite72Tile, sprite73Tile), axis=1)
        sprite70Full = numpy.concatenate((sprite70TopHalf, sprite70BottomHalf), axis=0)

        sprite70FullPIL = PIL.Image.fromarray(sprite70Full)
        sprite70FullPIL.save('Debug\\SpriteFarm\\sprite70.png')

        # Farm sprite8
        sprite80 = session.botsupport_manager().sprite(32)
        sprite81 = session.botsupport_manager().sprite(33)
        sprite82 = session.botsupport_manager().sprite(34)
        sprite83 = session.botsupport_manager().sprite(35)

        sprite80TileId = sprite80.tiles[0].tile_identifier
        sprite80Tile = session.botsupport_manager().tile(sprite80TileId).image_ndarray()

        sprite81TileId = sprite81.tiles[0].tile_identifier
        sprite81Tile = session.botsupport_manager().tile(sprite81TileId).image_ndarray()

        sprite82TileId = sprite82.tiles[0].tile_identifier
        sprite82Tile = session.botsupport_manager().tile(sprite82TileId).image_ndarray()
       
        sprite83TileId = sprite83.tiles[0].tile_identifier
        sprite83Tile = session.botsupport_manager().tile(sprite83TileId).image_ndarray()
       
        sprite80TopHalf = numpy.concatenate((sprite80Tile, sprite81Tile), axis=1)
        sprite80BottomHalf = numpy.concatenate((sprite82Tile, sprite83Tile), axis=1)
        sprite80Full = numpy.concatenate((sprite80TopHalf, sprite80BottomHalf), axis=0)

        sprite80FullPIL = PIL.Image.fromarray(sprite80Full)
        sprite80FullPIL.save('Debug\\SpriteFarm\\sprite80.png')

        # Farm sprite9
        sprite90 = session.botsupport_manager().sprite(36)
        sprite91 = session.botsupport_manager().sprite(37)
        sprite92 = session.botsupport_manager().sprite(38)
        sprite93 = session.botsupport_manager().sprite(39)

        sprite90TileId = sprite90.tiles[0].tile_identifier
        sprite90Tile = session.botsupport_manager().tile(sprite90TileId).image_ndarray()

        sprite91TileId = sprite91.tiles[0].tile_identifier
        sprite91Tile = session.botsupport_manager().tile(sprite91TileId).image_ndarray()

        sprite92TileId = sprite92.tiles[0].tile_identifier
        sprite92Tile = session.botsupport_manager().tile(sprite92TileId).image_ndarray()
       
        sprite93TileId = sprite93.tiles[0].tile_identifier
        sprite93Tile = session.botsupport_manager().tile(sprite93TileId).image_ndarray()
       
        sprite90TopHalf = numpy.concatenate((sprite90Tile, sprite91Tile), axis=1)
        sprite90BottomHalf = numpy.concatenate((sprite92Tile, sprite93Tile), axis=1)
        sprite90Full = numpy.concatenate((sprite90TopHalf, sprite90BottomHalf), axis=0)

        sprite90FullPIL = PIL.Image.fromarray(sprite90Full)
        sprite90FullPIL.save('Debug\\SpriteFarm\\sprite90.png')

    def NewSpriteSheet():
        workingDirectory = 'Debug\\SpriteFarm\\Workspace'
        initialDirectory = workingDirectory + '\\Initial'
        spriteMapPath = 'TemplateMatching\\Sheets\\SpriteSheet.png'
        trashDirectory = '.spriteTrash'
        workingDirectoryContent = os.listdir(workingDirectory)
        initialImages = os.listdir(initialDirectory)
        
        firstImagePath = str(initialImages.pop(0))
        firstImage = PIL.Image.open(initialDirectory  + '\\' + firstImagePath)
        firstImage = firstImage.resize((64, 64))
        firstImage.save(spriteMapPath)
        
        firstImageCharacter = firstImagePath.replace('.png', '')
        firstImageCharacter = firstImageCharacter.replace('_', ' ')
        firstImageCharacter = firstImageCharacter.replace(' down', '')
        firstImageCharacter = firstImageCharacter.replace(' up', '')
        firstImageCharacter = firstImageCharacter.replace(' side', '')

        if firstImageCharacter != 'Player':
            raise Exception('Initial images must be of Player')
        spriteMap = [
            firstImageCharacter
        ]
        os.rename(initialDirectory + '\\' + firstImagePath, trashDirectory + '\\' + firstImagePath)

        existingImage = firstImage
        existingImage = numpy.array(existingImage)
        
        
        for imagePath in initialImages:
            if imagePath.endswith(".png"):
                print(imagePath)
                newImage = PIL.Image.open(initialDirectory + '\\' + imagePath)
                newImage = numpy.array(newImage)
                newImage = PIL.Image.fromarray(newImage)
                newImage = newImage.resize((64, 64))
                existingImage = numpy.concatenate((existingImage, newImage), axis=1)
                newImageCharacter = imagePath.replace('.png', '')
                if "side" in newImageCharacter:
                    isSide = True 
                else:
                    isSide = False
                newImageCharacter = newImageCharacter.replace('_', ' ')
                newImageCharacter = newImageCharacter.replace(' down', '')
                newImageCharacter = newImageCharacter.replace(' up', '')
                newImageCharacter = newImageCharacter.replace(' side', '')
                spriteMap.append(newImageCharacter)
                os.rename(initialDirectory + '\\' + imagePath, trashDirectory + '\\' + imagePath)

                if isSide:
                    flippedImage = newImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
                    existingImage = numpy.concatenate((existingImage, flippedImage), axis=1)
                    spriteMap.append(newImageCharacter)
                    isSide = False

        
        for imagePath in workingDirectoryContent:
            if imagePath.endswith(".png"):
                print(imagePath)
                newImage = PIL.Image.open(workingDirectory + '\\' + imagePath)
                newImage = numpy.array(newImage)
                newImage = PIL.Image.fromarray(newImage)
                newImage = newImage.resize((64, 64))
                existingImage = numpy.concatenate((existingImage, newImage), axis=1)
                newImageCharacter = imagePath.replace('.png', '')
                if "side" in newImageCharacter:
                    isSide = True
                else:
                    isSide = False
                newImageCharacter = newImageCharacter.replace('_', ' ')
                newImageCharacter = newImageCharacter.replace(' down', '')
                newImageCharacter = newImageCharacter.replace(' up', '')
                newImageCharacter = newImageCharacter.replace(' side', '')
                spriteMap.append(newImageCharacter)
                os.rename(workingDirectory + '\\' + imagePath, trashDirectory + '\\' + imagePath)

                if isSide:
                    flippedImage = newImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
                    existingImage = numpy.concatenate((existingImage, flippedImage), axis=1)
                    spriteMap.append(newImageCharacter)
                    isSide = False
            
        spriteMap = json.dumps(spriteMap, indent = 4)
        spriteMap
        print(spriteMap)
        with open('TemplateMatching\\Sheets\\SpriteSheet.json', 'w') as outfile:
            outfile.write(spriteMap)
        existingImage = PIL.Image.fromarray(existingImage)
        existingImage.save(spriteMapPath)

    def UpdateSpriteSheet():
        workingDirectory = 'Debug\\SpriteFarm\\Workspace'
        spriteMapPath = 'TemplateMatching\\Sheets\\SpriteSheet.png'
        trashDirectory = '.spriteTrash'
        workingDirectoryContent = os.listdir(workingDirectory)
        existingImage = PIL.Image.open(spriteMapPath)
        existingImage = numpy.array(existingImage)
        spriteMap = json.load(open('TemplateMatching\\Sheets\\SpriteSheet.json'))

        for imagePath in workingDirectoryContent:
            if imagePath.endswith(".png"):
                print(imagePath)
                newImage = PIL.Image.open(workingDirectory + '\\' + imagePath)
                newImage = newImage.resize((64, 64))
                existingImage = numpy.concatenate((existingImage, newImage), axis=1)
                newImageCharacter = imagePath.replace('.png', '')
                if "side" in newImageCharacter:
                    isSide = True 
                else:
                    isSide = False
                newImageCharacter = newImageCharacter.replace('_', ' ')
                newImageCharacter = newImageCharacter.replace(' down', '')
                newImageCharacter = newImageCharacter.replace(' up', '')
                newImageCharacter = newImageCharacter.replace(' side', '')
                spriteMap.append(newImageCharacter)
                os.rename(workingDirectory + '\\' + imagePath, trashDirectory + '\\' + imagePath)

                if isSide:
                    flippedImage = newImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
                    existingImage = numpy.concatenate((existingImage, flippedImage), axis=1)
                    spriteMap.append(newImageCharacter)
                    isSide = False
            
        spriteMap = json.dumps(spriteMap, indent = 4)
        print(spriteMap)
        with open('TemplateMatching\\Sheets\\SpriteSheet.json', 'w') as outfile:
            outfile.write(spriteMap)
        existingImage = PIL.Image.fromarray(existingImage)
        existingImage.save(spriteMapPath)

    def SetInventoryItem0(session, index, item, quantity = 1, ):
        if index < 0 or index > 19:
            raise Exception('Index must be between 0 and 19')
        if quantity < 1 or quantity > 99:
            raise Exception('Quantity must be between 1 and 99')
        if item < 0 or item > 255:
            raise Exception('Item must be between 0 and 255')
        itemHex = GameData.Items[item]
        session.set_memory_value(0xD31E)
    