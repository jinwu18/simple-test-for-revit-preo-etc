import time

from loguru import logger
import pyautogui


while True:
    x, y = pyautogui.position()
    logger.info('鼠标当前所在位置：' + str(x) + ', ' + str(y))
    time.sleep(1)
