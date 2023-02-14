import bim_auto_base as bim

# 被按住的鼠标键（左键LEFT、右键RIGHT、中键滚轮MIDDLE）
middle = bim.MouseKey.MIDDLE
ctrl = bim.KeyboardKey.CTRL


def key_down():
    bim.left_corner_click()
    bim.center_pos_click()
    bim.key_press(ctrl)
    bim.mouse_press(middle)


def key_release():
    bim.key_release(ctrl)
    bim.mouse_release(middle)


def hot_key_down():
    bim.left_corner_click()
    bim.center_pos_click()
    bim.mouse_press(middle)


def hot_key_release():
    bim.mouse_release(middle)


def mouse_rotate():
    """鼠标按住后花圈"""
    hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.CIRCLE)
    hot_key_release()


def mouse_scroll_right_left():
    """鼠标按住向右拖动"""
    hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_RIGHT)
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_LEFT)
    hot_key_release()


def mouse_scroll_down_up():
    """鼠标按住后向下拖动"""
    hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_DOWN)
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_UP)
    hot_key_release()


def zoom_in_out():
    """鼠标滚轮缩放"""
    bim.center_pos_click()
    key_down()
    bim.mouse_scroll_up()
    bim.mouse_scroll_down()
    bim.mouse_scroll_down()
    bim.mouse_scroll_up()
    key_release()
    # bim.mouse_zoom()


def test_run():
    mouse_rotate()
    mouse_scroll_right_left()
    mouse_scroll_down_up()
    # zoom_in_out()


if __name__ == '__main__':
    for i in range(200):
        test_run()
