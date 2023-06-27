import pyautogui
import cv2
import numpy as np
import logging
import os
import sys
from matplotlib import pyplot as plt
import pytesseract
import cv2 as cv
import numpy as np
import sys
from PIL import Image

class MatchResult:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.width = endX - startX
        self.height = endY - startY  

class MatchTemplate: 
    def Match(session, template, threshold, masks = None, scale = 6):
        hres = 160 * scale
        vres = 144 * scale

        templatePath = "TemplateMatching\\" + template + ".png"
        debugPath = "Debug\MatchTemplate\\" + template + "\\"
        result = None

        screenshotOriginalDebugPath = debugPath + template +  "Original.png"
        screenshotMaskedDebugPath = debugPath + template + "Masked.png"
        screenshotResizedDebugPath = debugPath + template + "Resized.png"
        screenshotMatchedDebugPath = debugPath + template + "Matched.png"
        screenshotMatchedAreaDebugPath = debugPath + template + "MatchedArea.png"

        screenshot = session.screen_image()
        screenshot.save(screenshotOriginalDebugPath)
        screenshotResized = screenshot.resize((hres, vres))
        screenshotResized.save(screenshotResizedDebugPath)
        screenshot_color = cv2.cvtColor(np.array(screenshotResized), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot_color, cv2.COLOR_BGR2GRAY)
        if masks != None:
            logging.info("Masking screenshot")
            for mask in masks:
                cv2.rectangle(screenshot_color, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                cv2.rectangle(screenshot_color, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                logging.info("Saving masked screenshot to " + screenshotMaskedDebugPath)
                cv2.imwrite(screenshotMaskedDebugPath, screenshot_color)
                
        templateFile = cv2.imread(templatePath, 0)
                cv2.imwrite(screenshotMaskedDebugPath, screenshot_color)
                
        templateFile = cv2.imread(templatePath, 0)

        w, h = templateFile.shape[::-1]
        w, h = templateFile.shape[::-1]

        logging.info("Matching template " + templatePath + " with threshold " + str(threshold))
        matchResult = cv2.matchTemplate(screenshot_gray, templateFile, cv2.TM_CCOEFF_NORMED)
        matchResult = cv2.matchTemplate(screenshot_gray, templateFile, cv2.TM_CCOEFF_NORMED)
        location = np.where(matchResult >= threshold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(screenshot_color, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            cv2.rectangle(screenshot_color, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            if pt != None:
                logging.info("Template found")
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                (startX, startY) = maxLoc
                endX = startX + templateFile.shape[1]
                endY = startY + templateFile.shape[0]
                endX = startX + templateFile.shape[1]
                endY = startY + templateFile.shape[0]
                result = MatchResult(startX,startY,endX,endY)
                logging.info("Saving matched screenshot to " + screenshotMatchedDebugPath)
                cv2.imwrite(screenshotMatchedDebugPath, screenshot_color)

                logging.info("Saving matched area to " + screenshotMatchedAreaDebugPath)
                matchedArea = screenshotResized.crop((startX, startY, endX, endY))
                matchedArea.save(screenshotMatchedAreaDebugPath)

                resultObject = {
                    "screenshotOriginal": screenshot,
                    "screenshotResized": screenshotResized,
                    "screenshotMatched": screenshot_color,
                    "screenshotMatchedArea": matchedArea,
                    "region": result
                }
                return resultObject

class FindStuff:       
    def ConvoBox(session):
class FindStuff:       
    def ConvoBox(session):
        logging.info("Finding convo box")
        masks = [
            {
                "startX": 40,
                "startY": 624,
                "endX": 912,
                "endY": 816
            }
        ]
        ConvoBox = MatchTemplate.Match(session,"ConvoBox", 0.7, masks)

        if ConvoBox != None:
            logging.info("Convo box found")
            return ConvoBox
            logging.info("Convo box found")
            return ConvoBox
        else:
            logging.info("Convo box not found")
            logging.info("Convo box not found")
            return "NotFound"
        
    # TODO: Recheck these. If not working, check if they match the ConvoBox function
    # I basically merged the screenshot and findstuff function, as they were basically doing the same but just providing different outputs
    # def NurseJoyDialogBox():
    #     logging.info("Finding Nurse Joy dialog box")
    #     masks = [
    #         {
    #             "startX": 576,
    #             "startY": 376,
    #             "endX": 616,
    #             "endY": 528
    #         }
    #     ]
    #     ConvoBox = MatchTemplate.InGameWindow("TemplateMatching\\NurseJoyDialogBox.png", 0.8, masks)

    #     if ConvoBox != None:
    #         logging.info("Nurse Joy dialog box found")
    #         return ConvoBox    
    #     else:
    #         logging.info("Nurse Joy dialog box not found")
    #         return "NotFound"
        
    # def PCDialogBox():
    #     logging.info("Finding PC dialog box")
    #     masks = [
    #         {
    #             "startX": 48,
    #             "startY": 80,
    #             "endX": 88,
    #             "endY": 432
    #         }
    #     ]
    #     ConvoBox = MatchTemplate.InGameWindow("TemplateMatching\\PCDialogBox.png", 0.8, masks)

    #     if ConvoBox != None:
    #         logging.info("PC dialog box found") 
    #         return ConvoBox    
    #     else:
    #         logging.info("PC dialog box not found")
    #         return "NotFound"
        
class OCR:
    def ReadConvoBox(session):
    def ReadConvoBox(session):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        screenshot = FindStuff.ConvoBox(session)
        screenshot = FindStuff.ConvoBox(session)
        if screenshot != "NotFound":
            screenshotNp = np.array(screenshot["screenshotMatchedArea"])
            textRegion = screenshotNp[48:240, 48:816]
            cv2.imwrite("Debug\OCR\\textRegion.png", textRegion)
            text = pytesseract.image_to_string(textRegion, config='-l eng --oem 1 -c tessedit_char_whitelist=" .0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?\'"')
            print(text)



      