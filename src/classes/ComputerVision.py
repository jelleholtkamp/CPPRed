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
    def OnScreen(templatePath, threshold, masks = None):
        logging.info("Matching template " + templatePath + " with threshold " + str(threshold) + " on screen")
        debugPath = "Debug\MatchTemplate\OnScreen"
        result = None
        logging.info("Taking screenshot of entire screen")
        screenshot = pyautogui.screenshot()
        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        if masks != None:
            logging.info("Masking screenshot")
            for mask in masks:
                screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
                cv2.rectangle(screenshot, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                logging.info("Saving masked screenshot to " + screenshotMaskedDebugPath)
                cv2.imwrite(screenshotMaskedDebugPath, screenshot)
            
        template = cv2.imread(templatePath, 0)  

        w, h = template.shape[::-1]

        logging.info("Matching template " + templatePath + " with threshold " + str(threshold))
        matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        location = np.where(matchResult >= threshold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            if pt != None:
                logging.info("Template found")
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                (startX, startY) = maxLoc
                endX = startX + template.shape[1]
                endY = startY + template.shape[0]
                result = MatchResult(startX,startY,endX,endY)
                logging.info("Saving debug screenshot to " + screenshotDebugPath)
                cv2.imwrite(screenshotDebugPath, screenshot)
                return result

    def InGameWindow(templatePath, threshold, masks = None):
        debugPath = "Debug\MatchTemplate\InGameWindow"
        result = None

        screenshotDebugPath = debugPath + "\screenshot.png"
        gameWindow = FindStuff.GameWindow()

        if gameWindow != None:
            screenshot = pyautogui.screenshot(region=(gameWindow["region"].startX,gameWindow["region"].startY,gameWindow["region"].width,gameWindow["region"].height))
            print(screenshot)
            screenshot_color = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            screenshot_gray = cv2.cvtColor(screenshot_color, cv2.COLOR_BGR2GRAY)
            if masks != None:
                logging.info("Masking screenshot")
                for mask in masks:
                    screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
                    cv2.rectangle(screenshot_color, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                    logging.info("Saving masked screenshot to " + screenshotMaskedDebugPath)
                    cv2.imwrite(screenshotMaskedDebugPath, screenshot_color)
                
            template = cv2.imread(templatePath, 0)  

            w, h = template.shape[::-1]

            logging.info("Matching template " + templatePath + " with threshold " + str(threshold))
            matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            location = np.where(matchResult >= threshold)
            for pt in zip(*location[::-1]):
                cv2.rectangle(screenshot_color, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
                if pt != None:
                    logging.info("Template found")
                    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                    (startX, startY) = maxLoc
                    endX = startX + template.shape[1]
                    endY = startY + template.shape[0]
                    result = MatchResult(startX,startY,endX,endY)
                    logging.info("Saving debug screenshot to " + screenshotDebugPath)
                    cv2.imwrite(screenshotDebugPath, screenshot_color)
                    resultObject = {
                        "relativeRegion": result,
                        "absoluteRegion": gameWindow["region"]
                    }
                    return resultObject

class FindStuff:
    def WindowBar():
        logging.info("Finding window bar")
        WindowBarLocation = MatchTemplate.OnScreen("TemplateMatching\WindowBar.png",0.8)
        if WindowBarLocation != None:
            logging.info("Window bar found")
            global WindowBar
            WindowBar = WindowBarLocation
            return WindowBar
        else:
            logging.info("Window bar not found")
            return "NotFound"
        
    def GameWindow():
        logging.info("Finding game window")
        windowBar = FindStuff.WindowBar()

        if windowBar != None and windowBar != "NotFound":
            logging.info("Window bar found")
            gameWindow = windowBar
            gameWindow.startX  = windowBar.startX
            gameWindow.endX = windowBar.endX
            gameWindow.startY = windowBar.startY + windowBar.height
            gameWindow.endY = windowBar.endY + 864

            result = MatchResult(gameWindow.startX,gameWindow.startY,gameWindow.endX,gameWindow.endY)
            screenshot = pyautogui.screenshot(region=(gameWindow.startX,gameWindow.startY,result.width,result.height))

            gameWindow.width = result.width
            gameWindow.height = result.height

            screenshot.save("Debug\GameWindow\screenshot.png")
            result = {
                "screenshot": screenshot,
                "region": gameWindow
            }
            return result
        else:
            logging.info("Window bar not found")
        
    def ConvoBox():
        logging.info("Finding convo box")
        masks = [
            {
                "startX": 40,
                "startY": 624,
                "endX": 912,
                "endY": 816
            }
        ]
        ConvoBox = MatchTemplate.InGameWindow("TemplateMatching\\Convo.png", 0.8, masks)

        if ConvoBox != None:
            logging.info("Convo bar found")
            return ConvoBox    
        else:
            logging.info("Convo bar not found")
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
    def ReadConvoBox():
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        screenshot = FindStuff.ConvoBox()
        if screenshot != "NotFound":
            print(screenshot["absoluteRegion"].startX)
            print(screenshot["absoluteRegion"].startY)
            print(screenshot["absoluteRegion"].width)
            print(screenshot["absoluteRegion"].height)
            print("/////////////////////////////////")
            print(screenshot["relativeRegion"].startX)
            print(screenshot["relativeRegion"].startY)
            print(screenshot["relativeRegion"].width)
            print(screenshot["relativeRegion"].height)