#!/usr/bin/env python
# coding=utf-8

"""demo"""

__author__ = 'xiaocai'

import commands, cv2
import numpy as np

import adb

# 截图
adbkit = adb.adbKit()
adbkit.screenshots()

# 载入图像
target_img = cv2.imread("screencap.png")
find_img   = cv2.imread("images/btn_close_full.png")
find_height, find_width, find_channel = find_img.shape[::]

# 模板匹配
result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

# 计算位置
pointUpLeft   = max_loc
pointLowRight = (max_loc[0]+find_width, max_loc[1]+find_height)
pointCentre   = (max_loc[0]+(find_width/2), max_loc[1]+(find_height/2))

# 点击
adbkit.click(pointCentre)
exit()

# 画点
cv2.circle(target_img, pointUpLeft, 2, (255, 255, 255), -1)
cv2.circle(target_img, pointCentre, 2, (255, 255, 255), -1)
cv2.circle(target_img, pointLowRight, 2, (255, 255, 255), -1)

# 显示图片
cv2.namedWindow("Image")
cv2.imshow("Image", target_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 