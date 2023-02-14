import bim_auto_base as bim

# 被按住的鼠标键（左键LEFT、右键RIGHT、中键滚轮MIDDLE）
button = bim.MouseKey.MIDDLE
key = bim.KeyboardKey.SHIFT


def revit_hot_key_down():
    bim.left_corner_click()
    bim.center_pos_click()
    bim.key_press(key)
    bim.mouse_press(button)


def revit_hot_key_release():
    bim.key_release(key)
    bim.mouse_release(button)


def mouse_rectangle():
    bim.mouse_scroll_rectangle(1)


def mouse_rotate():
    """鼠标按住后花圈"""
    revit_hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.CIRCLE)
    revit_hot_key_release()


def mouse_scroll_right_left():
    """鼠标按住向右拖动"""
    revit_hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_RIGHT)
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.HOR_SCROLL_LEFT)
    revit_hot_key_release()


def mouse_scroll_down_up():
    """鼠标按住后向下拖动"""
    revit_hot_key_down()
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_DOWN)
    bim.mouse_scroll_and_drag(scroll_type=bim.ScrollType.VER_SCROLL_UP)
    revit_hot_key_release()


def zoom_in_out():
    """鼠标滚轮缩放"""
    bim.center_pos_click()
    bim.mouse_zoom()


def test_run():
    bim.module_pos_reset((1767, 210))
    # mouse_rectangle()
    zoom_in_out()
    # mouse_scroll_right_left()
    # mouse_scroll_down_up()
    # mouse_rotate()


if __name__ == '__main__':
    for i in range(2):
        test_run()
