# -*- coding: utf-8 -*-

import math
import pyautogui
from loguru import logger
import time


pyautogui.FAILSAFE = False
# pyautogui.PAUSE = 1


class KeyType:
    MOUSE = 1
    KEYBOARD = 2


class ScrollType:
    CIRCLE = 1                #以圆周滚动
    VER_SCROLL_DOWN = 2       #垂直向下滚动
    HOR_SCROLL_RIGHT = 3      #水平向右滚动
    VER_SCROLL_UP = 4         #垂直向上滚动
    HOR_SCROLL_LEFT = 5       #水平向左滚动


class MouseKey:
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'


class KeyboardKey:
    CTRL = 'Ctrl'
    SHIFT = 'Shift'
    FN = 'Fn'
    ALT = 'Alt'


def module_pos_reset(position):
    """鼠标点击操作"""
    pyautogui.moveTo(position)
    time.sleep(1)
    pyautogui.leftClick()


def mouse_click(button):
    """鼠标点击操作"""
    if button == 'left':
        pyautogui.leftClick()
    if button == 'middle':
        pyautogui.middleClick()
    if button == 'right':
        pyautogui.rightClick()
    time.sleep(1)


def mouse_press(button):
    """鼠标按下操作"""
    pyautogui.mouseDown(button=button)
    logger.info('按下鼠标：' + button)
    time.sleep(1)


def mouse_release(button):
    """鼠标释放"""
    pyautogui.mouseUp(button=button)
    logger.info('释放鼠标：' + button)


def key_press(key):
    """键盘按下操作"""
    pyautogui.keyDown(key)
    pyautogui.keyDown(key)
    logger.info('按下键盘按钮：' + key)
    time.sleep(1)


def key_release(key):
    """键盘释放"""
    pyautogui.keyUp(key)
    logger.info('释放键盘按钮：' + key)


def left_corner_click():
    """鼠标移动到左上角并点击鼠标左键"""
    x, y = 200, 200
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    logger.info('鼠标移动到' + str(x) + ', ' + str(y) + ', 并点击左键')


def bottom_right_pos_click():
    """鼠标移动到右下角并点击鼠标左键"""
    x, y = pyautogui.size()
    logger.info(str(x), str(y))

    pyautogui.moveTo(x-300, y-300)
    pyautogui.doubleClick()
    logger.info('鼠标移动到' + str(x-300) + ', ' + str(y-300) + ', 并点击左键')


def move_to_center():
    x, y = pyautogui.size()
    logger.info(str(x), str(y))

    pyautogui.moveTo(x/2, y/2)
    logger.info('鼠标移动到' + str(x/2) + ', ' + str(y/2))


def center_click(key):
    """根据给定参数点击鼠标"""
    move_to_center()
    if key == MouseKey.LEFT:
        pyautogui.leftClick()
        logger.info('点击鼠标左键')
    if key == MouseKey.RIGHT:
        pyautogui.rightClick()
        logger.info('点击鼠标右键')
    if key == MouseKey.MIDDLE:
        pyautogui.middleClick()
        logger.info('点击鼠标中键')


def center_pos_click():
    """鼠标移动到屏幕中键并点击鼠标左键"""
    move_to_center()
    pyautogui.leftClick()
    logger.info('点击鼠标左键')


def center_position_get():
    """屏幕中心微知获取"""
    x, y = pyautogui.size()
    logger.info('桌面分辨率为：' + str(x) + ', ' + str(y))
    return x/2, y/2


def mouse_zoom():
    """鼠标滚动缩放"""
    logger.info("开始缩放")
    x, y = center_position_get()
    ori_y = y
    max_y = y + 300
    y = y - 300
    speed = 10
    while y <= max_y:
        y += speed
        pyautogui.scroll(speed)
        logger.info(y)
    while y >= ori_y - 300:
        y -= speed
        pyautogui.scroll(-speed)
        logger.info(y)


def mouse_scroll_right():
    """鼠标向右滑动"""
    logger.info("开始水平向右移动")
    x, y = center_position_get()
    x = x - 300
    max_x = x + 300

    while x <= max_x:
        # 位置横移
        x += 2

        # 绝对坐标移动鼠标
        pyautogui.moveTo(int(x), int(y))


def mouse_scroll_left():
    """鼠标向右滑动"""
    logger.info("开始水平向左移动")
    x, y = center_position_get()
    x = x + 300
    min_x = x - 300

    while x >= min_x:
        # 位置横移
        x -= 2

        # 绝对坐标移动鼠标
        pyautogui.moveTo(int(x), int(y))


def mouse_scroll_up():
    """鼠标向上滑动"""
    logger.info("开始垂直向上移动")
    x, y = center_position_get()
    max_y = y - 300
    y = y + 300

    while y >= max_y:
        # 位置横移
        y -= 2

        # 绝对坐标移动鼠标
        pyautogui.moveTo(int(x), int(y))


def mouse_scroll_down():
    """鼠标向下滑动"""
    logger.info("开始垂直向下移动")
    x, y = center_position_get()
    max_y = y + 300
    y = y - 300

    while y <= max_y:
        # 位置横移
        y += 2

        # 绝对坐标移动鼠标
        pyautogui.moveTo(int(x), int(y))


def mouse_scroll_rectangle():
    """鼠标以200为半径绘制长方形"""
    logger.info("鼠标以200为半径绘制长方形")

    x, y = pyautogui.size()
    start_x = x-300
    start_y = y-300

    pyautogui.hotkey('w'+'a')
    for i in range(1):
        pyautogui.leftClick()
        pyautogui.moveTo(int(start_x), int(start_y))
        pyautogui.moveTo(int(start_x - 20 * (i - 1)), int(start_y - 20 * (i - 1)))
        pyautogui.moveTo(int(start_x + 20 * i), int(start_y))
        pyautogui.leftClick()
        pyautogui.moveTo(int(start_x + 20), int(start_y - 20 * i))
        pyautogui.leftClick()
        pyautogui.moveTo(int(start_x), int(start_y - 20 * i))
        pyautogui.leftClick()
        pyautogui.moveTo(int(start_x), int(start_y + 20 * i))
        pyautogui.leftClick()
    pyautogui.hotkey('Esc')


def mouse_scroll_circle():
    """鼠标以200为半径花圈"""
    logger.info("鼠标以200为半径花圈")
    min_angle = 0  # 每次循环角度计算
    max_angle = 360  # 最大角度
    spacing = 2  # 三角形的角度 可调整
    radius = 200  # 圆半径
    x, y = center_position_get()

    while min_angle <= max_angle:
        # 角度计算
        min_angle += spacing

        # x,y 绝对坐标计算
        x2 = ('%.0f' % (x + radius * math.cos(min_angle * math.pi / 180)))
        y2 = ('%.0f' % (y + radius * math.sin(min_angle * math.pi / 180)))

        # 绝对坐标移动鼠标
        pyautogui.moveTo(int(x2), int(y2))


def mouse_scroll_and_drag(scroll_type):
    """鼠标拖动并且不释放"""
    if scroll_type == 1:
        mouse_scroll_circle()
    if scroll_type == 2:
        mouse_scroll_down()
    if scroll_type == 3:
        mouse_scroll_right()
    if scroll_type == 4:
        mouse_scroll_up()
    if scroll_type == 5:
        mouse_scroll_left()

