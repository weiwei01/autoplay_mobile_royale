#!/usr/bin/env python
# coding=utf-8
"""demo"""

__author__ = 'xiaocai'

import cv2
import adb,uiDriver
import subprocess
import time




class Task():
	def getFreeResource(self):
		uiKit  = uiDriver.uiDriver()
		adbKit = adb.adbKit()
		#uiKit.useEvent('getFoodAndWood_decimal')
		uiKit.useEvent('changeMap')
		time.sleep(5)
		uiKit.useEvent('changeMap')
		time.sleep(5)

		#uiKit.useEvent('getWeaponAndGold_decimal')
		#uiKit.useEvent('changeMap')
		#time.sleep(5)
		#uiKit.useEvent('changeMap')
		#time.sleep(5)	
		#time.sleep(3)
		pos = uiKit.swipeUp()
		#pos = uiKit.findClick('free_coin_button.png')
		pos = uiKit.findClick('free_weapon_button.png')
		time.sleep(3)	
		pos = uiKit.swipeRight()
		#pos = uiKit.swipeRight()
		pos = uiKit.swipeRight()
		i=0
		for i in range(0,4):
			i += 1
			print(i)
			pos = uiKit.swipeDown()
			time.sleep(2)
		time.sleep(3)
		#uiKit.useEvent('getCheastAndRock_decimal')
		pos = uiKit.findClick('free_rock_button.png')
		pos = uiKit.findClick('special_chest_button1.png')
		time.sleep(3)
		i=0
		for i in range(0,7):
			i += 1
			print(i)
			pos = uiKit.swipeDown()
			time.sleep(2)
		time.sleep(3)
		#uiKit.useEvent('getFoodAndWood_decimal')
		pos = uiKit.findClick('free_wood_button.png')
		pos = uiKit.findClick('free_food_button.png')

while 1:
	task = Task()
	task.getFreeResource()
	time.sleep(5)
	uiKit  = uiDriver.uiDriver()
	#uiKit.useEvent('helpGuild_decimal')
	#pos = uiKit.findClick('cross_sign.png')

	time.sleep(600)
#uiKit.useEvent('helpGuild_decimal')
#uiKit.useEvent('getFreeResource_decimal')
#uiKit.useEvent('changeMap')

	
	
#command = 'adb shell swipe 200 200 300 300'
#adbKit.pythonCommand(command)

exit()
#adbKit.screenshots()

#pos = uiKit.findClick('start_game_icon.png')
#pos = uiKit.findClick('coin_button.png')
#pos = uiKit.findClick('free_coin_button.png')
#pos = uiKit.findClick('research_free_button.png')
#pos = uiKit.findClick('special_chest_button.png')
#pos = uiKit.findClick('receive_button.png')
#
#pos = uiKit.findClick('free_food_button.png')
#pos = uiKit.findClick('free_weapon_button.png')
#pos = uiKit.findClick('free_wood_button.png')
#pos = uiKit.swipeLeft()
#pos = uiKit.swipeRight()
#pos = uiKit.swipeUp()
#pos = uiKit.swipeDown()

