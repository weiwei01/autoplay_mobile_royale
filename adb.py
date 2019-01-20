#!/usr/bin/env python
# coding=utf-8

"""ADB"""

__author__ = 'xiaocai'

#import commands
import os
import subprocess

class adbKit(object):

    def screenshots(self, serialNumber=None):
        self.command('shell screencap -p /sdcard/screencap.png', serialNumber)
        self.command('pull /sdcard/screencap.png', serialNumber)

    def click(self, point, serialNumber=None):
        return self.command('shell input tap '+str(point[0])+' '+str(point[1]), serialNumber)
    def swipe(self, pointX, pointY, serialNumber=None):
        return self.command('shell input swipe '+str(pointX[0])+' '+str(pointX[1])+' '+str(pointY[0])+' '+str(pointY[1]), serialNumber)
    def command(self, cmd, serialNumber=None):
        cmdstr = 'adb '
        if serialNumber:
            cmdstr = cmdstr+'-s '+serialNumber
        #(status, output) = commands.getstatusoutput(cmdstr+cmd)
        (status, output) = subprocess.getstatusoutput(cmdstr+cmd)
        return [status, output]
    def pythonCommand(self, cmd):
        os.system(cmd)	
    def sendEvent(self, event, serialNumber=None):
        #os.system('adb shell sendevent '+str(event),)
        return self.command('shell sendevent '+str(event), serialNumber)

