import bim_auto_base as bim

# 被按住的鼠标键（左键LEFT、右键RIGHT、中键滚轮MIDDLE）
left = bim.MouseKey.LEFT
middle = bim.MouseKey.MIDDLE
right = bim.MouseKey.RIGHT
ctrl = bim.KeyboardKey.CTRL
shift = bim.KeyboardKey.SHIFT


def rotate_hot_key_down():
    bim.bottom_right_pos_click()
    bim.mouse_press(middle)
    bim.mouse_press(left)


def rotate_hot_key_release():
    bim.mouse_release(middle)
    bim.mouse_release(left)


def scroll_hot_key_down():
    bim.bottom_right_pos_click()
    bim.mouse_press(middle)
    bim.key_press(ctrl)


def scroll_hot_key_release():
    bim.mouse_release(middle)
    bim.key_release(ctrl)


def zoom_hot_key_down():
    bim.bottom_right_pos_click()
    bim.key_press(ctrl)
    bim.mouse_press(middle)
    

def zoom_hot_key_release():
    bim.key_release(ctrl)
    bim.mouse_release(middle)


def mouse_rotate():
    """鼠标按住后花圈"""
    rotate_hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.CIRCLE)
    rotate_hot_key_release()


def mouse_scroll_right_left():
    """鼠标按住向右拖动"""
    scroll_hot_key_down()
    # 向右滑动
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_RIGHT)
    # 向左滑动
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_LEFT)
    scroll_hot_key_release()


def zoom_in_out():
    """模型先放大再缩小"""
    zoom_hot_key_down()
    # 放大
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_UP)
    # 缩小
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_DOWN)
    zoom_hot_key_release()


def test_run():
    mouse_scroll_right_left()
    zoom_in_out()
    mouse_rotate()


if __name__ == '__main__':
    for i in range(2):
        test_run()
