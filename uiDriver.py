#!/usr/bin/env python
# coding=utf-8
import cv2
import adb,uiDriver
class uiDriver(object):
    def __init__(self):
        self.adb = adb.adbKit()   
    #def find(self, img, precision=0.9):
    def find(self, img, precision=0.5):
        # 截图
        self.adb.screenshots()

        # 载入图像
        targetImg = cv2.imread("screencap.png")
        findImg   = cv2.imread("images/"+img)
        findHeight, findWidth, findChannel = findImg.shape[::]

        # 模板匹配
        result = cv2.matchTemplate(targetImg, findImg, cv2.TM_CCOEFF_NORMED)
        minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
        print ('find: '+img, maxVal, maxLoc)

        # 计算位置
        pointUpLeft   = maxLoc
        pointLowRight = (maxLoc[0]+findWidth, maxLoc[1]+findHeight)
        pointCentre   = (maxLoc[0]+(findWidth/2), maxLoc[1]+(findHeight/2))

        # 匹配度要求
        if maxVal <= precision:
            print ('Can\'t find '+img, '(max:'+str(maxVal), 'expect:'+str(precision)+')')
            return False
                

        return pointCentre
	
    #def findClick(self, img, precision=0.9):
    def findClick(self, img, precision=0.3):
        point = self.find(img, precision)
        if not point:
            return False
        self.adb.click(point)
        return True
    def swipeLeft(self):
        pointX = [250, 250]  
        pointY = [300, 250]        
        self.adb.swipe(pointX, pointY)
        return True
    def swipeRight(self):
        pointX = [300, 250]  
        pointY = [250, 250]        
        self.adb.swipe(pointX, pointY)
        return True
    def swipeDown(self):
        pointX = [250, 300]  
        pointY = [250, 250]        
        self.adb.swipe(pointX, pointY)
        return True
    def swipeUp(self):
        pointX = [250, 250]  
        pointY = [250, 300]        
        self.adb.swipe(pointX, pointY)
        return True
    def useEvent(self, fileName):
        print(fileName)
        f = open(fileName + '.txt','r')
        x = f.read()
        f.close()

        inputCommand = list()
        for line in x.split('\n'):
			#print(line)
            command = 'adb shell sendevent ' + line
            print(command)
            self.adb.pythonCommand(command)
        return True